def get_morph(file):
    neko_morph = open(file,"r").readlines()
    article = []
    sentence = []
    for line in neko_morph:
        if "EOS" not in line:
            line = line.strip().replace("\t",",").split(",")
            morph_dict = {}
            morph_dict["表層形"] = line[0]
            morph_dict["基本形"] = line[7]
            morph_dict["品詞"] = line[1]
            morph_dict["品詞細分類１"] = line[2]
            sentence.append(morph_dict)
        if "句点" in line:
            article.append(sentence)
            sentence = []
    return article

if __name__ == '__main__':
    result = get_morph("./chapter04/neko.txt.mecab")
    for i in range(5):
        print(result[i])
