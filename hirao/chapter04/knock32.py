from knock30 import load_txt

OUTPUT_SIZE = 15

# 文ごとの形態素解析結果を受け取る
sentence_list = load_txt("neko.txt.mecab")

verb = []
for word_list in sentence_list:
    for i in range(len(word_list)):
        word = word_list[i]
        if word["pos"] == "動詞":
            verb.append(word["base"])
print(", ".join(verb[:OUTPUT_SIZE]))