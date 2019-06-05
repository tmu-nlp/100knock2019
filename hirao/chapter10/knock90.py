import gensim
from tqdm import tqdm
import subprocess
import numpy as np
import joblib
from operator import matmul

def main():
    print("loading word2vec model")
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

    p = subprocess.Popen(['wc', '-l', "../chapter09/knock81.txt"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, err = p.communicate()
    file_rows = int(result.strip().split()[0].decode('utf8'))

    # # 単語読み込み
    words_set = set()
    print("単語抽出")
    with tqdm(total=file_rows) as pbar, open("../chapter09/knock81.txt") as f:
        for line in f:
            words = line.split()
            for word in words:
                words_set.add(word)
            pbar.update(1)

    word_index = {}
    word_vectors = []
    for i, word in enumerate(tqdm(sorted(words_set))):
        word_index[word] = i
        try:
            vector = model[word]
        except:
            vector = np.zeros(300)
        word_vectors.append(vector)
    word_vectors = np.array(word_vectors)

    print("saving vectors")
    joblib.dump(word_vectors, "word_vectors", compress=3)
    joblib.dump(word_index, "word_index")
    print("finished saving")

def cos_sim(v1, v2):
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return matmul(v1, v2) / norm if norm else -1

def knock86_89():
    X = joblib.load("word_vectors")
    word_index = joblib.load("word_index")

    united_states = X[word_index["United_States"]]
    us = X[word_index["U.S"]]

    print("Result of knock86")
    print(united_states)

    print("Result of knock87")
    print(cos_sim(united_states, us))

    england = X[word_index["England"]]

    l = []
    for i, name in enumerate(tqdm(word_index.keys())):
        dis = cos_sim(england, X[i])
        l.append([name, dis])

    print("Result of knock88")
    for name, dis in sorted(l, key=lambda x: x[1], reverse=True)[:10]:
        print(f"{name}\t{dis}")

    spain = X[word_index["Spain"]]
    madrid = X[word_index["Madrid"]]
    athens = X[word_index["Athens"]]
    vec = spain - madrid + athens

    l = []
    for i, name in enumerate(tqdm(word_index.keys())):
        dis = cos_sim(vec, X[i])
        l.append([name, dis])

    print("Result of knock89")
    for name, dis in sorted(l, key=lambda x: x[1], reverse=True)[:10]:
        print(f"{name}\t{dis}")

if __name__ == "__main__":
    main()
    knock86_89()