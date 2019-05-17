'''
32. 動詞の原形
動詞の原形をすべて抽出せよ．
'''


from knock30 import morphines_read


def extract_verb_base():
    morphines, sentences = morphines_read()
    verb_base = []
    with open("verb_base_32.txt", "w") as fp:
        for morphine in morphines:
            if morphine["pos"] == "動詞":
                verb_base.append(morphine["base"])
                fp.write(morphine["base"] + "\n")
    return verb_base


if __name__ == "__main__":
    verb_base = extract_verb_base()
    # print(verb_base[0:12])