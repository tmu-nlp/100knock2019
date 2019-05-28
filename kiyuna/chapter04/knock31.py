'''
31. 動詞
動詞の表層形をすべて抽出せよ．
'''
import sys
from knock30 import mecab_into_sentences


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


if __name__ == '__main__':
    tgt = '動詞'
    res = []
    for sentence in mecab_into_sentences():
        # メモリには優しくないが，ネストは深くならない
        res.extend([d['surface'] for d in sentence if d['pos'] == tgt])
    message(f'{tgt}の表層形の数: {len(res)}')
    message(f'{tgt}の表層形の種類: {len(set(res))}')
    print('上から10個 ->', *res[:10])
