# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル
# (正例なら"+1"，負例なら"-1")と，その予測確率を計算するプログラムを実装せよ．

from sklearn.feature_extraction.text import TfidfVectorizer
from knock72 import create_feature, deserialize


def main() -> None:
    # model と vocal の読み込み
    model = deserialize("model")
    vocab = deserialize("vocabs")

    # sample.txt から素性を抽出し、ベクトル化する
    sentences, _ = create_feature("./sample.txt")
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    feature = vectorizer.fit_transform(sentences).toarray()

    # model.predict : データが分類されるクラスを予測
    # model.predict_proba : データが各クラスに分類される確率を求める
    pp = zip(model.predict(feature), model.predict_proba(feature))
    for predict, prob in pp:
        print(f"{int(predict):>3} : {max(prob):.6}")


if __name__ == "__main__":
    main()

"""
sample.txt
 head sentiment.txt > sample.txt

実行結果
  1 : 0.766867
 -1 : 0.878784
 -1 : 0.520656
  1 : 0.90806
 -1 : 0.67711
  1 : 0.736961
  1 : 0.765063
 -1 : 0.51283
  1 : 0.502839
 -1 : 0.52113
"""
