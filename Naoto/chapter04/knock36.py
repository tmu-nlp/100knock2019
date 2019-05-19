'''
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''


from knock30 import morphines_read
from collections import defaultdict


def word_frequency(mode="_"):
    morphines, sentences = morphines_read()
    word_freq_dic = defaultdict(lambda: 0)
    with open("word_freq_36.txt", "w") as fp:
        for line in morphines:
            word_freq_dic[line["surface"]] += 1
        if mode == "w":
            for k, v in sorted(word_freq_dic.items()):
                fp.write(k + " " + str(v) + "\n")
    return sorted(word_freq_dic.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    word_freq_dic = word_frequency("w")