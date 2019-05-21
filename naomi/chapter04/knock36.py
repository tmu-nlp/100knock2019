from knock30 import importmecab
from collections import defaultdict


# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．


def hist_words(sentences: list) -> dict:

    # words{単語:出現頻度}の初期化
    words = defaultdict(lambda: 0)

    for morphs in sentences:
        for m in morphs:
            if m['pos'] != '記号':
                words[m['base']] += 1

    return words


def hist_words_woPP(sentences: list) -> dict:

    # words{単語:出現頻度}の初期化
    words = defaultdict(lambda: 0)

    for morphs in sentences:
        for m in morphs:
            if (m['pos'] == '記号') or (m['pos'] == '助詞') or (m['pos'] == '助動詞'):
                continue
            else:
                words[m['base']] += 1

    return words


def main():
    path = 'neko.txt.mecab'
    wdict = hist_words(importmecab(path))
    sortwords = sorted(
                    wdict.items(),
                    key=lambda x: x[1],
                    reverse=True)

    with open('knock36.txt', 'w', encoding='utf-8') as f:
        print(sortwords, file=f)


if __name__ == '__main__':
    main()
