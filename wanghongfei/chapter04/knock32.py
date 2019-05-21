from knock30 import get_morph
result = get_morph("./chapter04/neko.txt.mecab")
for sentence in result:
    for morph in sentence:
        if morph["品詞"] == "動詞":
            print(morph["基本形"])