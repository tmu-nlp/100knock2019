from knock41 import get_chunk

if __name__ == "__main__":
    file_name = "./chapter05/neko.txt.cabocha"
    sentences = get_chunk(file_name)
    for sentence in sentences[:10]:
        for chunk in sentence:
            if chunk.dst != "-1" :
                print(chunk.morphs,"\t", \
                [i for i in sentence[int(chunk.dst)].morphs if "記号" not in i])