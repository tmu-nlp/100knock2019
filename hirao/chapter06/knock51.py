from knock50 import sentence_spliter
import re


def get_words(file_name):
    i = 0
    for sentence in sentence_spliter(file_name):
        for word in sentence.split():
            if i > 50:
                break
            yield word
            i += 1


if __name__ == "__main__":
    for word in get_words("nlp.txt"):
        print(word)
