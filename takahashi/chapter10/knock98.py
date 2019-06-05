"""
98. Ward法によるクラスタリング

96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
"""

from scipy.cluster.hierarchy import ward, dendrogram, linkage
from matplotlib import pyplot as plt
import sys, pathlib
import pandas as pd
sys.path.append(str(pathlib.Path() / ".." / "chapter08"))

from knock72 import serialize, deserialize

def main():
    # 国名に関するベクトルの読み込み
    features = deserialize("country.matrix")
    t_index = deserialize("country.index")

    # ward 法
    df = pd.DataFrame(features, t_index.keys())
    la = linkage(df, method="ward", metric="euclidean")

    # デンドログラムの表示
    dendrogram(la, labels=list(t_index.keys()), leaf_font_size=8)
    plt.show()

if __name__ == "__main__":
    main()