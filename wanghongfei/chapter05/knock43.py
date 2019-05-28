from knock41 import get_chunk

if __name__ == "__main__":
    file_name = "./neko.txt.cabocha"
    sentences = get_chunk(file_name)
    for sentence in sentences[:10]:
        for chunk in sentence:
            if "名詞" in [i[2] for i in chunk.morphs] \
            and "動詞" in [i[2] for i in sentence[int(chunk.dst)].morphs]:
                print(chunk.morphs, "\t", \
                [i for i in sentence[int(chunk.dst)].morphs if "記号" not in i])