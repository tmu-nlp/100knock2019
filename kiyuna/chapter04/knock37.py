'''
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''
import matplotlib.pyplot as plt
from collections import Counter
from knock30 import mecab_into_sentences


if __name__ == '__main__':
    num = 10
    cnter = Counter()
    for sentence in mecab_into_sentences():
        cnter += Counter(d['surface'] for d in sentence)

    labels, data = zip(*cnter.most_common(num))
    plt.bar(range(num), data)
    plt.title(f"頻度上位 {num} 語")
    plt.xticks(range(num), map(lambda x: f'"{x}"', labels))
    plt.xlabel("単語")
    plt.ylabel("出現頻度")
    plt.savefig('out37.png')
