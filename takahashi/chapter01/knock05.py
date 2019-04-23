# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer" という文から単語bi-gram，文字bi-gramを得よ．

from typing import Sequence, TypeVar

T = TypeVar("T")

def n_gram(target: Sequence[T], n: int) -> Sequence[T]:
    # シーケンスが文字列の場合 space を除去する
    if type(target) == str:
        target = target.replace(" ", "")

    # n-gram を作る (i 番目の文字or単語から n 番目の文字or単語を得る)
    result = []
    for i in range(len(target) - n + 1):
        result.append(target[i:i+n])

    # シーケンスがリストの場合にスペースで分割されている単語を連結する
    # 例 : ['I', 'am']-> 'I am'
    if type(target) == list:
        result = [" ".join(word) for word in result]

    return result

if __name__ == "__main__":
    seq = "I am an NLPer"

    print(n_gram(seq, 1)) # 文字 uni-gram
    print(n_gram(seq, 2)) # 文字 bi-gram
    print(n_gram(seq, 3)) # 文字 tri-gram

    seq = seq.split(" ")
    print(n_gram(seq, 1)) # 単語 uni-gram
    print(n_gram(seq, 2)) # 単語 bi-gram
    print(n_gram(seq, 3)) # 単語 tri-gram