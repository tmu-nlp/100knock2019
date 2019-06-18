'''
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
'''

from knock73 import serialize, deserialize, labels_sentences
from knock74 import prediction


def label_add(ans="features.txt", predict="prediction.txt", output="label_add.txt"):
    with open(ans, "r", encoding="latin-1") as f_ans, open(predict, "r", encoding="latin-1") as f_pre, open(output, "w", encoding="latin") as fw:
        ans_pre = list(zip(f_ans, f_pre))
        for line_ans, line_pre in ans_pre:
            if line_ans[0] == "-":
                fw.write(line_ans[:3] + line_pre)
            else:
                fw.write(line_ans[:2] + line_pre)


if __name__ == "__main__":
    label_add()
