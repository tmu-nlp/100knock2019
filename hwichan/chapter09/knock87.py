from scipy import io
import pickle
import numpy as np


def main():
    x300 = io.loadmat('knock_x300')['x300']

    with open('./pickles/t_dict', 'rb') as f:
        t_dict = pickle.load(f)

    vec1 = x300[t_dict['United_States_of_America']]
    vec2 = x300[t_dict['U.S.A']]
    # np.linalg.norm(vec)でvecの大きさを取ってこれる
    vec_norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    vec_dot = np.dot(vec1, vec2)
    print(vec_dot / vec_norm)  # 0.8863166440801677


if __name__ == "__main__":
    main()
