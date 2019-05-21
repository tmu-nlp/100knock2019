from knock30 import get_morph
result = get_morph("./chapter04/neko.txt.mecab")
for sentence in result:
    for morph in sentence:
        if morph["品詞細分類１"] == "サ変接続":
            print(morph["基本形"])