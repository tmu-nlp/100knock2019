from knock41 import load_chunk_list
import re

if __name__ == "__main__":
    pattern = re.compile('([\d,.，、．。, ]+)')
    sentence_list = load_chunk_list("neko.txt.cabocha")
    for sentence in sentence_list:
        for chunk in sentence:
            if chunk.srcs == []:
                continue
            for i in chunk.srcs:
                if "名詞" in map(lambda x: x.pos, sentence[i].morphs) and \
                        "動詞" in map(lambda x: x.pos, chunk.morphs):
                    left = pattern.sub("", sentence[i].morphstr).strip()
                    right = pattern.sub("", chunk.morphstr).strip()
                    # 最初の空白対策
                    if left == "":
                        break
                    print("{}\t{}".format(left, right))
