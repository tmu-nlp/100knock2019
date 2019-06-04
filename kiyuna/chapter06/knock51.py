'''
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
ただし，文の終端では空行を出力せよ．
'''
import sys
import re
from knock50 import nlp2line

res = set()


def nlp2word():
    for line in nlp2line():
        for word in line.split(' '):
            [res.add(x) for x in re.findall(r'[^a-zA-Z0-9]*', word) if x]
            yield word.strip('.,;:?!"()')


if __name__ == "__main__":
    sys.stdout.writelines('\n'.join(nlp2word()))

    # 出現する記号一覧
    print(*res, file=sys.stderr, sep='   ')
