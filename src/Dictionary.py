

class Dictionary:
	def __init__(self,file,subdir):
		self.file = file
		self.conversions = {}
		self.add_conversions()
		if not subdir:
			self.create_dict()

	def add_conversions(self):
		# I figured any way I did it would 
		# involve me writing at least the 
		# letters out, so I just did the 
		# whole thing
		self.conversions["a"] = 2
		self.conversions["b"] = 3
		self.conversions["c"] = 5
		self.conversions["d"] = 7
		self.conversions["e"] = 11
		self.conversions["f"] = 13
		self.conversions["g"] = 17
		self.conversions["h"] = 19
		self.conversions["i"] = 23
		self.conversions["j"] = 29
		self.conversions["k"] = 31
		self.conversions["l"] = 37
		self.conversions["m"] = 41
		self.conversions["n"] = 43
		self.conversions["o"] = 47
		self.conversions["p"] = 53
		self.conversions["q"] = 59
		self.conversions["r"] = 61
		self.conversions["s"] = 67
		self.conversions["t"] = 71
		self.conversions["u"] = 73
		self.conversions["v"] = 79
		self.conversions["w"] = 83
		self.conversions["x"] = 89
		self.conversions["y"] = 97
		self.conversions["z"] = 101

	def create_dict(self):
		self.words = {}
		f = open(self.file,"r")
		text = f.read()
		f.close()
		words = text.split("\n")
		for word in words:
			hash_val = 1
			for letter in word:
				hash_val *= self.conversions[letter]
			self.words[word] = hash_val

	def create_subdictionary(self):
		newdict =  Dictionary(self.file,True)
		newdict.words = self.words
		return newdict
	
	def remove(self,letter,contains,count):
		new_words = {}
		char_val = self.conversions[letter]**count
		for word in self.words:
			if contains:
				if self.words[word] % char_val != 0:
					new_words[word] = self.words[word]
			else:
				if self.words[word] % char_val == 0:
					new_words[word] = self.words[word]
		self.words = new_words
	
	def remove_position(self,letter,position,contains):
		new_words = {}
		for word in self.words:
			if word[position] == letter and not contains:
				new_words[word] = self.words[word]
			elif word[position] != letter and contains:
				new_words[word] = self.words[word]
		self.words = new_words

	def word_list(self):
		word_list = []
		for word in self.words:
			word_list.append(word)
		return word_list

	def print(self):
		for word in self.words:
			print("[{}]".format(word))
	

def check_contains(letter,word,count):
	for x in range(5):
		if letter == word[x]:
			count-=1
	return count < 1


def check_location(letter,word,position):
	return letter == word[position]
