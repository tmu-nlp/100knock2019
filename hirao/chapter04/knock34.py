from knock30 import load_txt
SIZE = 15

word_list = load_txt("neko.txt.mecab")

no = []

for i in range(len(word_list)-2):
    if word_list[i]["pos"] == "名詞" and word_list[i+1]["surface"] == "の" and word_list[i+2]["pos"] == "名詞":
        no.append(word_list[i]["surface"] + word_list[i+1]["surface"] + word_list[i+2]["surface"])
print(", ".join(no[:SIZE]))