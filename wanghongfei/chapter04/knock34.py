from knock30 import get_morph
result = get_morph("./chapter04/neko.txt.mecab")
for sentence in result:
    for morph in sentence:
        if sentence.index(morph) < len(sentence)-2 :
            next_index = "の" in sentence[sentence.index(morph) + 1].values()
            next_next_index = "名詞" in sentence[sentence.index(morph) + 2].values()
        else:
            next_index, next_next_index = False, False
        if morph["品詞"] == "名詞" and next_index and next_next_index:
            print(morph,sentence[sentence.index(morph) + 1], sentence[sentence.index(morph) + 2])