from Dictionary import Dictionary,check_contains,check_location
from Pidgeon import Pidgeon
#
import random as rand
import time


def run(file):
	dictionary = Dictionary(file,False)
	word = rand.choice(dictionary.word_list())
	for x in range(6):
		time.sleep(2)
		dictionary.print()
		while True:
			guess = input("_____\r")
			if dictionary.words.get(guess) != None:
				break
			else:
				print("Try again...")
		if guess == word:
			print("\033[42m{}\033[0m".format(word))
			break
		else:
			for i in range(5):
				letter = guess[i]
				if check_contains(letter,word):
					if check_location(letter,word,i):
						print("\033[42m{}\033[0m".format(letter),end="")
						dictionary.remove_position(letter,i,False)
					else:
						print("\033[43m{}\033[0m".format(letter),end="")
						dictionary.remove(letter,False)
						dictionary.remove_position(letter,i,True)
				else:
					print(letter,end="")
					dictionary.remove(letter,True)
			print()
	print(word)

def run_ai(file):
	pidgeon = Pidgeon(file)
	opponent = Dictionary(file,False)
	word = rand.choice(opponent.word_list())
	#word = "could"
	for x in range(6):
		guess = pidgeon.generate_word()
		if guess == word:
			print("[{0}] \033[42m{1}\033[0m".format(x+1,word))
			break
		else:
			print("[{}] ".format(x+1),end="")
			for i in range(5):
				letter = guess[i]
				count = 1
				for j in range(i):
					if guess[j] == letter:
						count += 1
				if pidgeon.dictionary.conversions.get(letter)!= None:
					if check_contains(letter,word,count):
						if check_location(letter,word,i):
							print("\033[42m{}\033[0m".format(letter),end="")
							pidgeon.dictionary.remove_position(letter,i,False)
						else:
							print("\033[43m{}\033[0m".format(letter),end="")
							pidgeon.dictionary.remove(letter,False,count)
							pidgeon.dictionary.remove_position(letter,i,True)
					else:
						print(letter,end="")
						pidgeon.dictionary.remove(letter,True,count)
						if count == 1:
							pidgeon.dictionary.conversions.pop(letter)
				else:
					print(letter,end="")
			print()
			time.sleep(.5)
			if x == 5:
				print(word)


if __name__ == '__main__':
	file = "../files/dictionary.txt"
	run_ai(file)
