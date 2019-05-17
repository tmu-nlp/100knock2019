'''
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''


from knock30 import morphines_read


def noun_sequence():
    morphines, sentences = morphines_read()
    noun_seq = []
    str_ = ""
    with open("noun_seq.txt", "w") as fp:
        for i in range(len(morphines) - 1):
            j = i
            while morphines[j]["pos"] == "名詞":
                j += 1
                if j > len(morphines):
                    break
                str_ += morphines[j]["surface"]
            if (j - i) >= 2:
                noun_seq.append(str_)
                fp.write(str_ + "\n")
            str_ = ""
    return noun_seq


if __name__ == "__main__":
    noun_seq = noun_sequence()