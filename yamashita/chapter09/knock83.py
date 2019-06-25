from tqdm import tqdm
from sklearn.externals import joblib
from collections import defaultdict
import subprocess


def main():
    count_tc = defaultdict(int)
    count_t = defaultdict(int)
    count_c = defaultdict(int)
    n = 0
    p = subprocess.Popen(['wc', '-l', 'result_knock82.txt'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, err = p.communicate()
    filesize = int(result.strip().split()[0].decode('utf-8'))

    with tqdm(total=filesize) as pbar, open('result_knock82.txt', 'r', encoding='utf-8') as i_file:
        for line in i_file:
            n += 1
            t, cs = line.split('\t')
            for c in cs.split():
                count_tc[f'{t}\t{c}'] += 1
                count_t[t] += 1
                count_c[c] += 1
            pbar.update(1)

    joblib.dump(count_tc, 'count_tc', compress=True)
    joblib.dump(count_t, 'count_t')
    joblib.dump(count_c, 'count_c')
    joblib.dump(n, 'n_count')
    print('finish')


if __name__ == '__main__':
    main()
