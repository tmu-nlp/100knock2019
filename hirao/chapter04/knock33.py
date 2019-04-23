from knock30 import load_txt
SIZE = 15

word_list = load_txt("neko.txt.mecab")

sahen = []
for i in range(len(word_list)):
    word = word_list[i]
    if word["pos1"] == "サ変接続":
        sahen.append(word["surface"])
print(", ".join(sahen[:SIZE]))
