from scipy import io
import pickle
import numpy as np


def cos_similarity(vec1, vec2):
    vec_norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    if vec_norm == 0:  # vec_normが０の場合は計算できないためエラーが出る
        return -1
    else:
        return np.dot(vec1, vec2) / vec_norm


def main():
    x300 = io.loadmat('knock_x300')['x300']

    with open('./pickles/t_dict', 'rb') as f:
        t_dict = pickle.load(f)  # key:word, value:index

    vec1 = x300[t_dict['England']]

    cos_similarities = []
    # すべての単語に対してcos_simを計算し、その中から上位１０位を取りだす
    for word, index in t_dict.items():
        if word == 'England':
            continue
        vec2 = x300[index]
        cos_sim = cos_similarity(vec1, vec2)
        cos_similarities.append((cos_sim, word))

    for n, similarity in enumerate(sorted(cos_similarities, reverse=True)):
        if n == 10:
            break
        print(similarity[1], similarity[0])


if __name__ == "__main__":
    main()


# Scotland 0.6306329662449524
# Australia 0.5811857484228181
# Wales 0.5581619544402054
# France 0.5499429555218962
# Italy 0.5393738358894061
# Spain 0.5334460269477225
# Ireland 0.5331514621592243
# Germany 0.49707254198580186
# Kingdom 0.4757557119991289
# Japan 0.4748371448825131

