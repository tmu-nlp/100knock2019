"""
91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
"""
import pickle
from collections import OrderedDict
from scipy import io
import numpy as np


fname_dict_index_t = r'C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter09\dict_index_t'
fname_matrix_x_300 = r'C:\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter09\matrix_x_300'
in_f = "family.txt"
out_f = "family_out.txt"

with open (fname_dict_index_t, "rb") as f:
    dict_index_t = pickle.load(f)

keys = list(dict_index_t.keys())

matrix_x_300 = io.loadmat(fname_matrix_x_300)["matrix_x_300"]

with open(in_f, 'rt') as in_f, open(out_f, 'wt') as out_f:
    
    for line in in_f:
        words = line.split(" ")
        
        
        try:
            vect = matrix_x_300[dict_index_t[words[1]]] - matrix_x_300[dict_index_t[words[0]]] + matrix_x_300[dict_index_t[words[2]]]
            ans_index = 0
            ans_max = -1
            result = ""
            for i in range(0, len(dict_index_t)) :
                norm = np.linalg.norm(vect) * np.linalg.norm(matrix_x_300[i])
                
                if norm != 0:
                    value = np.dot(vect, matrix_x_300[i]) / norm
                else:
                    value = -1
                
                if value > ans_max:
                    ans_index = i
                    ans_max = value

            result = keys[ans_index]
        
        except KeyError:
            result=""
            ans_max = -1

        try:
            print("{} {} {} " .format(line.strip(), result, ans_max))    
            print("{} {} {} " .format(line.strip(), result, ans_max), file=out_f)
        except:
            print("error\n{},  {},".format(ans_index, keys[ans_index]))


