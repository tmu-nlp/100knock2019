wordX = "paraparaparadise"
wordY = "paragraph"

X_bigram = []
Y_bigram = []
count=0
temp = ""

for i in range(len(wordX)-1):
    temp = wordX[count] + wordX[count+1]
    X_bigram.append(temp)
    count +=1

count=0
for i in range(len(wordY)-1):
    temp = wordY[count] + wordY[count+1]
    Y_bigram.append(temp)
    count +=1

X_bigram = set(X_bigram)
Y_bigram = set(Y_bigram)

union =set()
intersection =set()
difference =set()


union = X_bigram.union(Y_bigram)
intersection  = X_bigram.intersection(Y_bigram)
difference = X_bigram.difference(Y_bigram)

print("X_bigram=" + format( X_bigram))
print("Y_bigram" + format(Y_bigram))

print ("和集合" + format(union))
print("積集合" + format(intersection))
print("差集合" + format(difference))


print("X内に含まれるか：" + format({"se"} <= X_bigram))
print("Y内に含まれるか：" + format({"se"} <= Y_bigram))

