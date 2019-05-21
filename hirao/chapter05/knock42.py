from knock41 import load_chunk_list
import re

if __name__ == "__main__":
    pattern = re.compile('([\d,.，、．。, ]+)')
    sentence_list = load_chunk_list("neko.txt.cabocha")
    for sentence in sentence_list:
        for chunk in sentence:
            # 係元があるものだけ表示
            if chunk.srcs == []:
                continue
            for i in chunk.srcs:
                left = pattern.sub("", sentence[i].morphstr).strip()
                right = pattern.sub("", chunk.morphstr).strip()
                # 最初の空白対策
                if left == "":
                    break
                print("{}\t{}".format(left, right))
