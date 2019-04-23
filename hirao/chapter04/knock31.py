from knock30 import load_txt
SIZE = 15

word_list = load_txt("neko.txt.mecab")

verb = []
for i in range(len(word_list)):
    if word_list[i]["pos"] == "動詞":
        verb.append(word_list[i]["surface"])
print(", ".join(verb[:SIZE]))