from knock51 import get_words
from nltk.stem.porter import PorterStemmer as PS

if __name__ == "__main__":
    # ステミングするヤツ
    ps = PS()
    for word in get_words("nlp.txt"):
        print(word + "\t" + ps.stem(word))
