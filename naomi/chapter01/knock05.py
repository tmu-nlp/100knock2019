sentence='I am an NLPer.'



def word_bi_gram(sentence):
    wngram=[]
    sentence=sentence.replace(","," ")
    sentence=sentence.replace("."," ")
    words=sentence.split()

    for index in range(len(words)-1):
        wngram.append(words[index] + " " + words[index+1])

    print(wngram)

def char_bi_gram(sentence):
    cngram=[]
    sentence=sentence.replace(",","")
    sentence=sentence.replace(".","")
    sentence=sentence.replace(" ","")

    for index in range(len(sentence)-1):
        cngram.append(sentence[index]+" "+sentence[index+1])

    print(cngram)


word_bi_gram(sentence)
char_bi_gram(sentence)
