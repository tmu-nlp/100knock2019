'''
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．\
    ただし，文の終端では空行を出力せよ．
'''
import re


def word_exract(input_: str, output_: str):
    with open(input_) as f, open(output_, "w") as fw:
        for line in f:
            words = re.findall("[a-zA-Z0-9]{2,}", line)
            for word in words:
                print(word, file=fw)
            fw.write("\n")


if __name__ == "__main__":
    input_ = "nlp_s_d_50.txt"
    output_ = "nlp_words_51.txt"
    # output_ = "nlp_words_51_2.txt"
    word_exract(input_, output_)
