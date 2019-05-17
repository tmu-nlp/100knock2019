from knock30 import load_txt
import collections
SIZE = 15

sentence_list = load_txt("neko.txt.mecab")
# 文である必要がないので、単語ごとにバラす(2次元 -> 1次元)
word_list = [flatten for inner in sentence_list for flatten in inner]
words = list(map(lambda x: x["surface"], word_list))
# counterで数える
counter = collections.Counter(words)

# 頻度が高い順に出力
for (value, count) in counter.most_common()[:SIZE]:
    print(value, count)