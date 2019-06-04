from nltk.stem import PorterStemmer

words = open("./words.txt", "r").readlines()
ps = PorterStemmer()
for word in words:
    word = word.strip("\n")
    print(word, "\t", ps.stem(word))

