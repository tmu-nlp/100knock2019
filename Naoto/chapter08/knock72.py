'''
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
'''

import re
from knock71 import is_stopword_takahashi
from nltk.stem.porter import PorterStemmer as PS


def nlp2line(f_name='sentiment.txt'):
    sentences = []
    sentence_word_list = []
    word_list = []
    reg = re.compile(r'''
        (?<=[.;:?!])    # (. or ; or : or ? or !) に続いて
        \s              # 空白文字
        (?=[A-Z])       # 英大文字が続く場合だけマッチする
        ''', flags=re.VERBOSE)
    with open(f_name, "r", encoding='latin-1') as f:
        for line in map(lambda x: x.rstrip(), f):
            if not line:
                continue
            for res_line in reg.split(line):
                sentences.append(res_line)
    for i, sentence in enumerate(sentences):
        words = re.findall("[a-zA-Z0-9]{2,}", sentence)
        for word in words:
            word_list.append(word)
        sentence_word_list.append(word_list)
    for i, sentence in enumerate(sentence_word_list):
        len_sentence = len(sentence)
        for j in range(1, len_sentence):
            if is_stopword_takahashi(word):
                sentence_word_list[i].pop(j)
    ps = PS()
    len_word_list = len(sentence_word_list)
    for i in range(len_word_list):
        len_sentence = len(sentence)
        for j in range(1, len_sentence):
            sentence_word_list[i][j] = ps.stem(sentence_word_list[i][j])
    return sentence_word_list


if __name__ == "__main__":
    sentence_word_list = nlp2line()
    with open("features.txt", "w", encoding="latin-1") as f:
        for sentence in sentence_word_list:
            f.write(" ".join(sentence) + "\n")
