'''
32. 動詞の原形
動詞の原形をすべて抽出せよ．
'''
import sys
from knock30 import mecab_into_sentences


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


if __name__ == '__main__':
    tgt = '動詞'
    res = []
    for sentence in mecab_into_sentences():
        res.extend([d['base'] for d in sentence if d['pos'] == tgt])
    message(f'{tgt}の原形の数: {len(res)}')
    message(f'{tgt}の原形の種類: {len(set(res))}')
    print('上から10個 ->', *res[:10])
