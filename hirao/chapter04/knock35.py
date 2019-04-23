from knock30 import load_txt
SIZE = 15
nouns = []
l = 0
r = 0

word_list = load_txt("neko.txt.mecab")

for i in range(len(word_list)):
    word = word_list[i]

    if word["pos"] == "名詞":
        r += 1
    else:
        if r-l > 1 and word_list[i-1]["pos"] == "名詞":
            nouns.append("".join(list(map(lambda x: x["surface"], word_list[l:r]))))
        r += 1
        l = r

print(nouns[:SIZE])