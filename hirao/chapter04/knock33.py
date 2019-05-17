from knock30 import load_txt

OUTPUT_SIZE = 15

sentence_list = load_txt("neko.txt.mecab")

sahen = []
for word_list in sentence_list:
    for i in range(len(word_list)):
        word = word_list[i]
        if word["pos1"] == "サ変接続":
            sahen.append(word["surface"])
print(", ".join(sahen[:OUTPUT_SIZE]))