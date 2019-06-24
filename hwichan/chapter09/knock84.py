import pickle
from collections import OrderedDict
from scipy import sparse, io
from math import log


def main():
    N = 68081672
    with open('./pickles/count_tc', 'rb') as tc_file, \
            open('./pickles/count_t', 'rb') as t_file, \
            open('./pickles/count_c', 'rb') as c_file:
        count_tc = pickle.load(tc_file)  # 単語\t文脈語: 出現回数
        count_t = pickle.load(t_file)  # 単語: 出現回数
        count_c = pickle.load(c_file)  # 文脈語: 出現回数

    # 行列作成 key（単語）だけをfor文で回し、単語:インデックスのdictを作成
    t_dict = OrderedDict((word, index) for index, word in enumerate(count_t.keys()))  # 行
    c_dict = OrderedDict((word, index) for index, word in enumerate(count_c.keys()))  # 列

    # sparse.lil_matrix((n, m))でn行m列の疎行列（すべての要素が０）を作成
    x = sparse.lil_matrix((len(t_dict), len(c_dict)))
    print('finish x')

    for tc, count in count_tc.items():
        # 単語\t文脈語の出現回数が１０以下ならば要素は０のまま
        if count < 10:
            continue

        tc_list = tc.split('\t')
        t = tc_list[0]
        c = tc_list[1]

        # ppimiを計算し、その（単語,文脈語）要素をppmiに変更
        ppmi = max(log((N * count) / (count_t[t] * count_c[c])), 0)
        x[t_dict[t], c_dict[c]] = ppmi

    io.savemat('knock_x', {'x': x})
    with open('./pickles/t_dict', 'wb') as f:
        pickle.dump(t_dict, f)


if __name__ == "__main__":
    main()
