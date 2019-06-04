'''
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
'''

import os
import sys
import subprocess
import re
import xml.etree.ElementTree as ET

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # cd .


def message(text="", CR=False):
    text = "\r" + text if CR else text + "\n"
    sys.stderr.write("\33[92m" + text + "\33[0m")


def POS(input_, output_):
    characters = "a-zA-Z0-9"
    with open(input_) as f, open(output_, "w") as fw:
        for line in f:
            word = re.search("<word>([\S.,]+)</word>", line)
            if word is not None:
                print(word.group(1) + "\t", end="", file=fw)
            lemma = re.search("<lemma>([\S.,]+)</lemma>", line)
            if lemma is not None:
                print(lemma.group(1) + "\t", end="", file=fw)
            POS = re.search("<POS>([\S.,]+)</POS>", line)
            if POS is not None:
                print(POS.group(1), file=fw)


def POS_xml(input_, output_):
    with open(output_, "w") as fw:
        tree = ET.parse(input_)
        root = tree.getroot()
        for word, lemma, POS in zip(root.iter("word"), root.iter("lemma"), root.iter("POS")):
            print(f"{word.text}\t{lemma.text}\t{POS.text}", file=fw)


if __name__ == "__main__":
    input_ = "nlp.txt.xml"
    is_xml = sys.argv[1:] == ["xml"]
    output_xml = "POS_54_xml.txt"
    output_ = "POS_54.txt"
    if is_xml:
        message("[*] xml.etree.ElementTree")
        POS_xml(input_, output_xml)
        subprocess.run(f"diff -s {output_xml} {output_}".split())
    else:
        message("[*] regex")
        POS(input_, output_)
        subprocess.run(f"diff -s {output_} {output_xml}".split())
