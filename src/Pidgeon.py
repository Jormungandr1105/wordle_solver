# Introducing Pidgeon, the Wordle Solver
from Dictionary import Dictionary
import random as rand

class Pidgeon:
	def __init__(self,dict_file):
		self.dictionary = Dictionary(dict_file,False)

	def generate_word(self):
		return rand.choice(self.dictionary.word_list())

	def get_letter_pop(self):
		chars = []
		for letter in self.dictionary.conversions:
			char_val = self.dictionary.conversions[letter]
			
