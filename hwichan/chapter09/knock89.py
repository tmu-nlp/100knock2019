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

    vec_Spain = x300[t_dict['Spain']]
    vec_Madrid = x300[t_dict['Madrid']]
    vec_Athens = x300[t_dict['Athens']]
    vec1 = vec_Spain - vec_Madrid + vec_Athens

    cos_similarities = []
    for word, index in t_dict.items():
        vec2 = x300[index]
        cos_sim = cos_similarity(vec1, vec2)
        cos_similarities.append((cos_sim, word))

    for n, similarity in enumerate(sorted(cos_similarities, reverse=True)):
        if n == 10:
            break
        print(similarity[1], similarity[0])


if __name__ == "__main__":
    main()


# Spain 0.8605481845263976
# Sweden 0.8412422088550879
# Austria 0.8206232527873395
# Italy 0.7960821028954921
# Denmark 0.7787400805430473
# France 0.7692031639754034
# Belgium 0.7648885909500438
# Germany 0.764830342550759
# Télévisions 0.750591549972748
# Greece 0.7390682528304385

