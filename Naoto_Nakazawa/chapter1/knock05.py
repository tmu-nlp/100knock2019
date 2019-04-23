def make_ngram(arr: [], n: int):
   return list(arr[i:i + n] for i in range(len(arr) + 1 - n)) 

# def make_ngram_word(arr: [], n: int):

target = "I am an NLPer"

print(make_ngram(target.split(), 2))
print(make_ngram(target, 2))