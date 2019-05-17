'''
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
'''


from knock30 import morphines_read


def extract_A_B():
    '''2つの名詞が「の」で連結されている名詞句を抽出'''
    morphines, sentences = morphines_read()
    A_B = []
    with open("AのB.txt", "w") as fp:
        for i in range(len(morphines) - 2):
            if morphines[i]["pos"] == "名詞" and morphines[i+1]["surface"] == "の"\
                and morphines[i+2]["pos"] == "名詞":
                str_ = morphines[i]["surface"] + morphines[i+1]["surface"]\
                    + morphines[i+2]["surface"]
                A_B.append(str_)
                fp.write(str_ + "\n")
    return A_B


if __name__ == "__main__":
    A_B = extract_A_B()