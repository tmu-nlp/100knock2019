'''
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
'''
import sys
from knock30 import mecab_into_sentences


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


if __name__ == '__main__':
    tgt = 'AのB'
    res = []
    for sentence in mecab_into_sentences():
        for a, no, b in zip(sentence, sentence[1:], sentence[2:]):
            if (a['pos'], no['surface'], b['pos']) == ('名詞', 'の', '名詞'):
                res.append(''.join(map(lambda x: x['surface'], (a, no, b))))
    message(f'{tgt}の数: {len(res)}')
    message(f'{tgt}の種類: {len(set(res))}')
    print('上から10個 ->', *res[:10])
