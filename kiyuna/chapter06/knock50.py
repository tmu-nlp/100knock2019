'''
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
入力された文書を1行1文の形式で出力せよ．
'''
import sys
import re


def nlp2line(f_name='nlp.txt'):
    reg = re.compile(r'''
        (?<=[.;:?!])    # (. or ; or : or ? or !) に続いて
        \s              # 空白文字
        (?=[A-Z])       # 英大文字が続く場合だけマッチする
        ''', flags=re.VERBOSE)
    with open(f_name) as f:
        for line in map(lambda x: x.rstrip(), f):
            if not line:
                continue
            for res_line in reg.split(line):
                yield res_line


if __name__ == "__main__":
    sys.stdout.writelines('\n'.join(nlp2line()))
