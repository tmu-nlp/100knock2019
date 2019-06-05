from collections import defaultdict
from tqdm import tqdm
import subprocess
import joblib


def token_context():
    print("Loading text")
    count_tc = defaultdict(int)
    count_t = defaultdict(int)
    count_c = defaultdict(int)
    n = 0
    p = subprocess.Popen(['wc', '-l', "knock82.txt"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, err = p.communicate()
    file_rows = int(result.strip().split()[0].decode('utf8'))
    with tqdm(total=file_rows) as pbar, open("knock82.txt") as f:
        for line in f:
            t, c = line.rstrip().split("\t")
            n += 1
            count_tc[f"{t} {c}"] += 1
            count_t[t] += 1
            count_c[c] += 1
            pbar.update(1)

    print("Saving count_tc")
    joblib.dump(count_tc, "count_tc", compress=3)
    print("Saving count_t")
    joblib.dump(count_t, "count_t")
    print("Saving count_c")
    joblib.dump(count_c, "count_c")
    print("Saving count_n")
    joblib.dump(n, "count_n")
    print("Finished")

# 6minくらいかかる
if __name__ == "__main__":
    token_context()
