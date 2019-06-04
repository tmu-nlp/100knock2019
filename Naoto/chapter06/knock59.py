'''
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．\
    入れ子になっている名詞句もすべて表示すること．
'''

import xml.etree.ElementTree as ET
import os
import sys
import subprocess


os.chdir(os.path.dirname(os.path.abspath(__file__)))  # cd .


def message(text="", CR=False):
    text = "\r" + text if CR else text + "\n"
    sys.stderr.write("\33[92m" + text + "\33[0m")


def S_formula_analytics(input_, output_):
    count = 0
    status = 0
    paren = 0
    with open(output_, "w") as f:
        tree = ET.parse(input_)
        root = tree.getroot()
        for parse in root.iter("parse"):
            word = ""
            for character in parse.text:
                word += character
                if status == 0:
                    if character == "(":
                        word = ""
                    if "NP" in word:
                        status = 1
                        word = ""
                        continue
                else:
                    if character == " ":
                        word = ""
                    elif character == "(":
                        paren += 1
                        word = ""
                    elif character == ")":
                        paren -= 1
                        if len(word) > 1:
                            print(word[:-1], end=" ")
                            # print(word[:-1], end=" ", file=output_)
                        word = ""
                    if paren == -1:
                        word = ""
                        status = 0
                        paren = 0
                        print("\n", end="")
                        # print("\n", end="", file=output_)
                        continue
            print("\n\n", end="")
            # print("\n\n", end="", file=output_)
            count += 1


if __name__ == "__main__":
    input_ = "nlp.txt.xml"
    output_ = "S_formula_59.txt"
    S_formula_analytics(input_, output_)
