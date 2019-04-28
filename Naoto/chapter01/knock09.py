def typoglycemia(word: str) -> str:
    if len(word) <= 4:
        return word
    from random import sample
    while True:
        result = word[0] + ''.join(sample(word[1:-1], len(word) - 2)) + word[-1]
        if result != word:
            return result

def typoglycemia_sentence(sentence: str) -> str:
    words = sentence.split(' ')
    return ' '.join(typoglycemia(word) for word in words)

print(typoglycemia_sentence("On January 24th Apple computer will introduce Macintosh"))
print(typoglycemia_sentence("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))




