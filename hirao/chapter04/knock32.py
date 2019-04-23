from knock30 import load_txt
SIZE = 15

word_list = load_txt("neko.txt.mecab")

verb = []
for i in range(len(word_list)):
    word = word_list[i]
    if word["pos"] == "動詞":
        verb.append(word["base"])
print(", ".join(verb[:SIZE]))