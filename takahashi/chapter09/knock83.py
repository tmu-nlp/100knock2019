"""

83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

  - f(t,c): 単語tと文脈語cの共起回数
  - f(t,∗): 単語tの出現回数
  - f(∗,c): 文脈語cの出現回数
  - N: 単語と文脈語のペアの総出現回数

"""
from collections import defaultdict
from typing import Dict
from tqdm import tqdm
import redis, pickle, pandas
import sys
from knock80 import file_reader


def main():
    tc = defaultdict(int)
    t = defaultdict(int)
    c = defaultdict(int)
    n = 0

    r = redis.Redis(host="localhost", port=6379, db=0)
    line = file_reader("./results/knock82.output.tsv")
    for _ in tqdm(range(68070373)):  # tsv ファイルの行数, 要変更
        # カンマ区切りのファイルを一行ずつ読み込む
        tokens = line.__next__().strip().split("\t")
        if len(tokens) < 2:
            continue

        tc["\t".join(tokens)] += 1
        t[tokens[0]] += 1
        c[tokens[1]] += 1
        n += 1

    r.set("knock83.tc", pickle.dumps(tc, protocol=-1))
    r.set("knock83.t", pickle.dumps(t, protocol=-1))
    r.set("knock83.c", pickle.dumps(c, protocol=-1))
    r.set("knock83.n", n)

    print(f"N={n}")


if __name__ == "__main__":
    main()
