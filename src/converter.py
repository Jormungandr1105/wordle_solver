file = "../files/dictionary.txt"
f = open(file,"r")
text = f.read()
f.close()
f = open(file,"w+")
words = text.split("\n")
for word in words:
	word = word.replace("\'","").replace(",","")
	f.write("{}\n".format(word))
f.close()
