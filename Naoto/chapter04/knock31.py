'''
31. 動詞
動詞の表層形をすべて抽出せよ．
'''


from knock30 import morphines_read


def extract_verb_surface():
    morphines, sentences = morphines_read()
    verb_surface = []
    with open("verb_surface_31.txt", "w") as fp:
        for morphine in morphines:
            if morphine["pos"] == "動詞":
                verb_surface.append(morphine["surface"])
                fp.write(morphine["surface"] + "\n")
    return verb_surface


if __name__ == "__main__":
    verb_surface = extract_verb_surface()
    # print(verb_surface[0:12])