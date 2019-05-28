'''
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''
import sys
import pprint
from knock30 import mecab_into_sentences


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


if __name__ == '__main__':
    tgt = '名詞+'
    res = []
    for sentence in mecab_into_sentences():
        nouns = []
        for d in sentence:
            if d['pos'] == '名詞':
                nouns.append(d['surface'])
            else:
                if len(nouns) > 1:      # 名詞の連結
                    res.append((len(nouns), ''.join(nouns)))
                nouns = []
        if len(nouns) > 1:              # 番兵を使って解決できる
            res.append((len(nouns), ''.join(nouns)))
    message(f'{tgt}の数: {len(res)}')
    message(f'{tgt}の種類: {len(set(res))}')
    print('--- 上から 5 個 ---')
    pprint.pprint(res[:5])
    res.sort(reverse=True)
    print('--- 大きい順に 5 個 ---')
    pprint.pprint(res[:5])
