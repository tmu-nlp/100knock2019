'''
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
'''

import re


def sencence_distinction(input_: str, output_: str):
    with open(input_) as f, open(output_, "w") as fw:
        count = 0
        for line in f:
            line = line.rstrip() + " A"
            match_list = re.findall(".+?[.;:?!]\s[A-Z]", line)
            l = len(match_list)
            if l == 0:
                continue
            match_list.insert(0, match_list[0][0])
            match_list[1] = match_list[1][1:]
            for i in range(l):
                fw.write(match_list[i][-1] + match_list[i+1][:-2] + "\n")


if __name__ == "__main__":
    input_ = "nlp.txt"
    output_ = "nlp_s_d.txt"
    sencence_distinction(input_, output_)
