import random

def typoglycemia(string1):
    split_str=string1.split(" ")
    out=[]
    for i in range(0,len(split_str)):
        # consider a word
        word=split_str[i]
        if len(word)>4:
            # make a random sentence with middle part
            randomlist=random.sample(word[1:len(word)-1],len(word)-2)
            randomstr = ''.join(randomlist)
            print(word[0]+randomstr+word[len(word)-1])
            out.append(word[0]+randomstr+word[len(word)-1]+" ")
        else:
            out.append(word+" ")
    print(''.join(out))
typoglycemia("I couldn't believe that I could actually understand what \
    I was reading : the phenomenal power of the human mind.")
