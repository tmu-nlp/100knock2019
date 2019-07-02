'''
98. Ward 法によるクラスタリング
96 の単語ベクトルに対して，Ward 法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
'''
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from knock96 import extract_vecs_of_countries

if __name__ == '__main__':
    X, labels = extract_vecs_of_countries()

    # Ward 法による階層型クラスタリング
    df = pd.DataFrame(X, labels)
    z = linkage(df, method="ward")

    # クラスタリング結果をデンドログラムとして可視化
    plt.figure(figsize=(40, 25))
    dendrogram(z, labels=labels,
               leaf_font_size=10.5,     # 横軸の文字の大きさを指定
               color_threshold=2.,      # ユークリッド平方距離が 2 以上を同色で表示
               )
    plt.savefig("out98.png")


'''
* linkage
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

* dendrogram
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html
'''
