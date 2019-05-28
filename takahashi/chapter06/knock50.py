# 50. 文区切り
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
# 入力された文書を1行1文の形式で出力せよ．

from typing import List
import re


def divide_into_sentences() -> List[str]:
    sentences = []
    pattern = r"""
        (
            ^             # 行頭
            .*?           # 任意の最短 0 文字以上
            [\.|;|\?|\!]  # . or ; or : or ? or !
        ) 
        \s                # 空白
        (
            [A-Z].*       # 英大文字
        )
        """
    regex = re.compile(pattern, re.MULTILINE | re.VERBOSE | re.DOTALL)
    for line in open("../data/nlp.txt", encoding="utf-8"):
        line = line.strip()

        while line != "":
            m = regex.match(line)
            if m:
                sentences.append(m.group(1))
                line = m.group(2)
            else:
                sentences.append(line)
                line = ""

    return sentences


if __name__ == "__main__":
    for sentence in divide_into_sentences():
        print(sentence)
