'''
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，\
    モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
'''

from knock73 import serialize, deserialize, labels_sentences
from sklearn.model_selection import cross_validate

# def labels_sentences(feature="features.txt", num, fold):
#     labels = []
#     sentences = []
#     with open(feature, "r", encoding="latin-1") as f:
#         pbar = tqdm(total=10662)
#         for i, line in enumerate(f):
#             if i > 10662*(num)/fold and i < 10662*(num + 1)/fold:
#                 continue
#             line = line.rstrip()
#             labels.append(int(line[:2]))
#             sentences.append(line[3:])
#             pbar.update(1)
#     pbar.close()
#     return labels, sentences


def cross_validation():
    model = deserialize("model")
    features = deserialize("features")
    labels = deserialize("labels")
    score_funcs = [
        'accuracy',
        'precision',
        'recall',
        'f1',
    ]
    scores = cross_validate(model, features, labels, cv=5, scoring=score_funcs)
    print('正解率:', scores['test_accuracy'].mean())
    print('適合率:', scores['test_precision'].mean())
    print('再現率:', scores['test_recall'].mean())
    print('F1値:', scores['test_f1'].mean())


if __name__ == "__main__":
    cross_validation()
