import sys
from collections import defaultdict

dic = defaultdict(lambda: 0)
input_ = [x for x in sys.stdin]

for line in input_:
    dic[line.split('\t')[0]] += 1


def key_selector(s: str):
    return dic[s.split('\t')[0]]

for line in sorted(input_, key= key_selector, reverse = True):
    print(line, end = "")
