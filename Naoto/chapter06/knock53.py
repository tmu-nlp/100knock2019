'''
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．\
    また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
'''

import re


def Tokenization(input_, output_):
    with open(input_) as f, open(output_, "w") as fw:
        for line in f:
            word = re.search("<word>([a-zA-Z0-9]{2,})</word>", line)
            if word is not None:
                print(word.group(1), file=fw)


if __name__ == "__main__":
    input_ = "nlp.txt.xml"
    output_ = "Tokenization_53.txt"
    Tokenization(input_, output_)
