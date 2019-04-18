sentence = "I am an NLPer"
sentence_list = sentence.split()
 
sentence_list.extend("")

word_bigram = []
letter_bigram = []
count=0

temp = ""
 
for i in range(len(sentence_list)-1):
    temp = sentence_list[count]  + " " +sentence_list[count+1]
    word_bigram.append(temp)
    count +=1
  
print(word_bigram)

joinletter = "".join(sentence_list)

count=0

for i in range(len(joinletter)-1):
    temp = joinletter[count] + joinletter[count+1]
    letter_bigram.append(temp)
    count +=1

print(letter_bigram)