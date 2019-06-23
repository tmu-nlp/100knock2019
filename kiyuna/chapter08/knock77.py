'''
77. 正解率の計測
76の出力を受け取り，
予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
'''
from collections import defaultdict
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import classification_report

POS = "+1"
NEG = "-1"

#
# 混同行列 confusion matrix
#
matrix = defaultdict(int)
for ans, pred, _ in map(lambda x: x.split('\t'), open('out76')):
    matrix[ans, pred] += 1

TP = matrix[POS, POS]  #    pred
TN = matrix[NEG, NEG]  #   P   N
FP = matrix[NEG, POS]  # [[TP, FN]   P  ans
FN = matrix[POS, NEG]  #  [FP, TN]]  N

ans, pred, _ = zip(*map(lambda x: x.split('\t'), open('out76')))
y_ans = list(map(int, ans))
y_pred = list(map(int, pred))
print("混同行列:")
print(confusion_matrix(y_ans, y_pred))


#                        TP + TN
# 正解率 Accuracy = ───────────────────（正や負と予測したデータのうち，
#                   TP + FP + FN + TN   実際にそうであるものの割合）
#   * FP と FN の重要度について特に考慮しなくても良いとき
accuracy = (TP + TN) / (TP + FP + FN + TN)
assert accuracy == accuracy_score(y_ans, y_pred)
print("正解率:", accuracy)


#                       TP
# 適合率 Precision = ─────────（正と予測したデータのうち，実際に正であるものの割合）
#                    TP + FP
#   * あきらかに陽性と分かりやすいものだけを見つけたいとき
#     FN が許容できる，FP があっては困るとき
precision = TP / (TP + FP)
assert precision == precision_score(y_ans, y_pred)
print("適合率:", precision)


#                    TP
# 再現率 Recall = ─────────（実際に正であるもののうち，正であると予測されたものの割合）
#                 TP + FN
#   * 怪しいものはとりあえず全て見つけ出したいとき
#     FP が許容できる，FN があっては困るとき
recall = TP / (TP + FN)
assert recall == recall_score(y_ans, y_pred)
print("再現率:", recall)


#                  2 * Precision * recall
# F値 F-measure = ────────────────────────（適合率と再現率の調和平均）
#                    Precision + recall
#   * 適合率と再現率の両者のバランスが極端に悪くないものを作りたいとき
f1 = 2 * precision * recall / (precision + recall)
assert f1 == f1_score(y_ans, y_pred)
print("F1スコア:", f1)


print(classification_report(y_ans, y_pred))


'''
* 機械学習で分類問題のモデルを評価する指標について
https://blog.amedama.jp/entry/2017/12/18/005311

- TP: True Positive
    正しく陽性と判定できた場合
- TP: True Negative
    正しく陰性と判定できた場合
- FP: False Positive
    本来は陰性なところを、誤って陽性と判定してしまった場合
- FN: False Negative
    本来は陽性なところを、誤って陰性と判定してしまった場合
'''
