'''
05. n-gram
与えられたシーケンス（文字列やリストなど）から n-gram を作る関数を作成せよ．
この関数を用い，"I am an NLPer" という文から単語 bi-gram，文字 bi-gram を得よ．
'''
# https://docs.python.org/ja/3/library/typing.html
from typing import Sequence


def n_gram(seq: Sequence, n: int) -> list:
    """ NGram Tokenizer

    任意のシーケンスに対して，連続した n 個を先頭から順番に切り出す．

    Args:
        seq (Sequence): 切り出す対象
        n (int): 切り出す長さ

    Returns:
        list: seq のタイプと同じ N-gram のリスト

    """
    # list(zip(*[seq[i:] for i in range(n)]))
    return [seq[i:i + n] for i in range(len(seq) - n + 1)]


if __name__ == '__main__':
    sentence = "I am an NLPer"

    words = sentence.split()
    chars = sentence            # .replace(' ', '_') を付けると空白がわかりやすくなる

    bi_gram_w = n_gram(words, n=2)
    bi_gram_c = n_gram(chars, n=2)

    print('単語 bi-gram:', bi_gram_w)
    print('文字 bi-gram:', bi_gram_c)

    '''
    * [seq[i:i + n] for i in range(len(seq) - n + 1)] の場合

        [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
        ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

    * list(zip(*[seq[i:] for i in range(n)])) の場合

        [('I', 'am'), ('am', 'an'), ('an', 'NLPer')]
        [('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', 'a'), ('a', 'n'),
         ('n', ' '), (' ', 'N'), ('N', 'L'), ('L', 'P'), ('P', 'e'), ('e', 'r')]
    '''

    # help(n_gram)
