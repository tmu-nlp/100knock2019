'''
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
'''


from knock30 import morphines_read


def extract_sahen_noun():
    '''サ変接続の名詞を抽出'''
    morphines, sentences = morphines_read()
    sahen_noun = []
    with open("sahen_noun_33.txt", "w") as fp:
        for line in morphines:
            if line["pos"] == "名詞" and line["pos1"] == "sahen":
                sahen_noun.append(line["surface"])
                fp.write(line["surface"] + "\n")
    return sahen_noun


if __name__ == "__main__":
    sahen_noun = extract_sahen_noun()
    # print(verb_base[0:12])