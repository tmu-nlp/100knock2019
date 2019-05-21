'''
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
'''
import sys
from knock30 import mecab_into_sentences


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


if __name__ == '__main__':
    tgt = 'サ変接続'
    res = []
    for sentence in mecab_into_sentences():
        res.extend([d['surface'] for d in sentence if d['pos1'] == tgt])
    message(f'{tgt}の名詞の数: {len(res)}')
    message(f'{tgt}の名詞の種類: {len(set(res))}')
    print('上から10個 ->', *res[:10])
