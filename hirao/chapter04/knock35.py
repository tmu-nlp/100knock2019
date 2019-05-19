from knock30 import load_txt

OUTPUT_SIZE = 15
nouns = []

sentence_list = load_txt("neko.txt.mecab")

for word_list in sentence_list:
    l = 0
    r = 0
    for i in range(len(word_list)):
        word = word_list[i]
        if word["pos"] == "名詞":
            r += 1
        else:
            if r-l > 1 and word_list[i-1]["pos"] == "名詞":
                nouns.append("".join(list(map(lambda x: x["surface"], word_list[l:r]))))
            r += 1
            l = r

print(nouns[:OUTPUT_SIZE])