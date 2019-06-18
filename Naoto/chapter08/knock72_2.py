'''
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
'''

import re
from knock71 import is_stopword
from nltk.stem.porter import PorterStemmer as PS
from tqdm import tqdm


def nlp2line(f_name='sentiment.txt'):
    sentences = []
    sentence_word_list = []
    word_list = []
    reg = re.compile(r'''
        (?<=[.;:?!])    # (. or ; or : or ? or !) に続いて
        \s              # 空白文字
        (?=[A-Z])       # 英大文字が続く場合だけマッチする
        ''', flags=re.VERBOSE)
    count = 0
    with open(f_name, "r", encoding='latin-1') as f:
        for line in map(lambda x: x.rstrip(), f):
            if not line:
                continue
            for res_line in reg.split(line):
                sentences.append(res_line)
            if count == 0:
                print(sentences)
                count = 1
    pbar = tqdm(total=len(sentences))
    with open("word_features.txt", "w", encoding="latin-1") as f:
        for i, sentence in enumerate(sentences):
            words = re.findall("[a-zA-Z0-9-']+", sentence)
            for word in words:
                f.write(word + " ")
            f.write("\n")
            # sentence_word_list.append(word_list)
            pbar.update(1)
    pbar.close()


def stopword_removal(word_features="word_features.txt", no_stopword_features="no_stopword_features.txt"):
    pbar = tqdm(total=10662)
    with open(word_features, "r", encoding="latin-1") as f, open(no_stopword_features, "w", encoding="latin-1") as fw:
        for line in f:
            label_words = line.rstrip().split(" ")
            label = label_words[0]
            words = label_words[1:]
            fw.write(label)
            for i, word in enumerate(words):
                if is_stopword(word):
                    continue
                fw.write(" " + word)
            pbar.update(1)
            fw.write("\n")
    pbar.close()


def stemming(no_stopword_features="no_stopword_features.txt", features="features.txt"):
    pbar = tqdm(total=10662)
    with open(no_stopword_features, "r", encoding="latin-1") as f, open(features, "w", encoding="latin-1") as fw:
        ps = PS()
        for line in f:
            label_words = line.rstrip().split(" ")
            label = label_words[0]
            words = label_words[1:]
            fw.write(label)
            for word in words:
                word = ps.stem(word)
                fw.write(" " + word)
            fw.write("\n")
            pbar.update(1)
    pbar.close()


if __name__ == "__main__":
    # sentence_word_list = nlp2line()
    # nlp2line()
    stopword_removal()
    stemming()
    # with open("features.txt", "w", encoding="latin-1") as f:
    #     for sentence in sentence_word_list:
    #         f.write(" ".join(sentence) + "\n")
