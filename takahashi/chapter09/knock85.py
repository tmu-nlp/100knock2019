"""

85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．

"""

from sklearn.decomposition import TruncatedSVD, PCA
from scipy.io import savemat
import redis, pickle


def main():
    r = redis.Redis(host="localhost", port=6379, db=0)
    matrix = pickle.loads(r.get("knock84.sparse_matrix"))

    # 圧縮する次元数の指定
    pca = TruncatedSVD(n_components=300)
    processed = pca.fit_transform(matrix)

    # 行列の保存
    savemat("knock85.matrix", {"knock85.matrix": processed})


if __name__ == "__main__":
    main()
