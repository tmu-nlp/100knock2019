"""

82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

  - ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
  - 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．

"""

from random import randint
from typing import List, Tuple, Any
from tqdm import tqdm
import pickle
from knock80 import file_reader
import csv
import pandas
import redis


# 前後 d 単語の文脈語のリストを返す
# e.g.
#   words = [..., that, advocates, stateless, societies, often, ...]
#   current -> stateless, d -> 2
#   return [that, advocates, societies, often]
def get_context(current: int, words: List[str]) -> str:
    d = randint(1, 5)
    left = words[max(current - d, 0) : current]
    right = words[current + 1 : current + 1 + d]

    return left + right


def main(line_num: int) -> None:
    line = file_reader("./results/knock81.output")
    output_file_path = "./results/knock82.output.tsv"
    with open(output_file_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        batch = []
        for i in tqdm(range(1, line_num + 1)):
            words = line.__next__().strip().split()
            for idx, word in enumerate(words):
                for context in get_context(idx, words):
                    batch.append([word, context])

            if i % 10000 == 0:
                writer.writerows(batch)
                batch = []
        writer.writerows(batch)


if __name__ == "__main__":
    line_num = 252693  # wc -l ./results/knock81.output
    # main()
    main(line_num)


"""

実行結果

$ head -n20 ./results/knock82.output.tsv

Anarchism	is
Anarchism	a
Anarchism	political
Anarchism	philosophy
Anarchism	that
is	Anarchism
is	a
is	political
is	philosophy
a	Anarchism
a	is
a	political
a	philosophy
a	that
political	Anarchism
political	is
political	a
political	philosophy
political	that
political	advocates

"""
