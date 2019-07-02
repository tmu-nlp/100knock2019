'''
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''
import sys
import pickle
import word2vec
import scipy.io as sio
from sklearn.metrics.pairwise import cosine_similarity as cos_sim


def message(text="", CR=False):
    text = "\r" + text if CR else text + "\n"
    sys.stderr.write("\33[92m" + text + "\33[0m")


def load(file_name):
    with open(f"../chapter09/pickles/{file_name}.pkl", 'rb') as f_in:
        data = pickle.load(f_in)
    return data


def chapter09(in_data, out_path):
    ft = load('ft')
    t2i = {token: i for i, token in enumerate(ft)}
    vec = sio.loadmat('../chapter09/pickles/X_300.mat')['X_300']
    with open(out_path, 'w') as f_out:
        for a, b, _ in in_data:
            try:
                cs = cos_sim([vec[t2i[a]]], [vec[t2i[b]]])[0][0]
            except Exception as e:
                cs = -1
            print(f'{a} {b} {_} {cs:f}', file=f_out)


def chapter10(in_data, out_path):
    model = word2vec.load('out90.bin')
    with open(out_path, 'w') as f_out:
        for a, b, _ in in_data:
            try:
                cs = cos_sim([model[a]], [model[b]])[0][0]
            except Exception as e:
                cs = -1
            print(f'{a} {b} {_} {cs:f}', file=f_out)


if __name__ == '__main__':
    import zipfile
    in_data = []
    with zipfile.PyZipFile('./wordsim353.zip') as myzip:
        with myzip.open('combined.tab') as f_in:
            for line in map(lambda x: x.decode().rstrip(), f_in):
                in_data.append(line.split('\t'))
    message('[*] chapter09')
    chapter09(in_data, 'out94_ch09.txt')
    message('[*] chapter10')
    chapter10(in_data, 'out94_ch10.txt')


'''
* zipfile モジュール
- https://docs.python.org/ja/3/library/zipfile.html
'''
