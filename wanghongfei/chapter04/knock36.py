from knock30 import get_morph
result = get_morph("./chapter04/neko.txt.mecab")
frequency = {}
for sentence in result:
    for morph in sentence:
        frequency.setdefault(morph["基本形"], 0)
        frequency[morph["基本形"]] += 1
print(frequency)
