from scipy.sparse import lil_matrix, csr_matrix
from tqdm import tqdm
import joblib
import time
import math

def main():
    print("loading data...")
    start = time.time()
    count_tc = joblib.load("count_tc")
    count_t = joblib.load("count_t")
    count_c = joblib.load("count_c")
    count_n = joblib.load("count_n")
    take_time = time.time() - start
    print(f"load finished time:{take_time}sec")

    t_size = len(count_t)
    c_size = len(count_c)

    # 疎行列に入れる時のindex決め
    t_index = {}
    c_index = {}
    print("set t_index")
    for i, key in enumerate(count_t.keys()):
        t_index[key] = i
    joblib.dump(t_index, "t_index")
    print("set c_index")
    for i, key in enumerate(count_c.keys()):
        c_index[key] = i
    joblib.dump(c_index, "c_index")

    # 疎行列初期化
    X = lil_matrix((t_size, c_size))
    print("set sparse matrix")
    for t_c, f_tc in tqdm(count_tc.items()):
        if f_tc >= 10:
            t, c = t_c.split()
            ppmi = max(0, math.log2(count_n * f_tc / count_t[t] /count_c[c]))
            X[t_index[t], c_index[c]] = ppmi
    X = X.tocsr()
    joblib.dump(X, "X", compress=3)

if __name__ == "__main__":
    main()
