# 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

from knock50 import divide_into_sentences
from typing import List


def cut_out_words() -> List[List[str]]:
    word_list = []
    for sentence in divide_into_sentences():
        words = sentence.split(" ")
        # 1 行 1 単語の形式で出力するので記号を除去する
        word_list.append([word.rstrip(".,;:?!") for word in words])
    return word_list


if __name__ == "__main__":
    for words in cut_out_words():
        for word in words:
            print(word)
        print("")
