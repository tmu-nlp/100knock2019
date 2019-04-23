from knock30 import load_txt
import collections
SIZE = 15

word_list = load_txt("neko.txt.mecab")
words = list(map(lambda x: x["surface"], word_list))
counter = collections.Counter(words)

for (value, count) in counter.most_common()[:SIZE]:
    print(value, count)