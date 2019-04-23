
def char_bi_gram(sentence):
    cngram=[]
    sentence=sentence.replace(",","")
    sentence=sentence.replace(".","")
    sentence=sentence.replace(" ","")

    for index in range(len(sentence)-1):
        cngram.append(sentence[index]+" "+sentence[index+1])
#    print(cngram)
    return cngram

X=char_bi_gram('paraparaparadise')
Y=char_bi_gram('paragraph')

# Sum
Sum_X_Y = set(X)|set(Y)
# Product
Intersect_X_Y=set(X)&set(Y)
# Difference
Diff_X_Y=set(X)-set(Y)
Diff_Y_X=set(Y)-set(X)

# Check if 'se'exists in a set
print('s e' in set(X))
print('s e' in set(Y))


#print(Sum_X_Y)
#print(Intersect_X_Y)
#print(Diff_X_Y)
#print(Diff_Y_X)
