"""
80. コーパスの整形
文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである． 
ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう． 
そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，
各トークンに以下の処理を施し，単語から記号を除去せよ．

 - トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
 - 空文字列となったトークンは削除

以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
"""

from typing import List, Generator
from memory_profiler import profile
from tqdm import tqdm


def file_reader(filepath: str) -> Generator[str, None, None]:
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def tokenize(words: List[str]) -> str:
    return " ".join([word.strip(":.,!?;:()[]'\"") for word in words])


def main(path: str, line_num: int) -> None:
    output = "./results/knock80.output"
    line = file_reader(path)
    with open(output, "w", encoding="utf-8") as f:
        for _ in tqdm(range(line_num)):
            processed = tokenize(line.__next__().strip().split())
            if len(processed) < 1:
                continue
            f.write(processed + "\n")


if __name__ == "__main__":
    # file_path = "../data/enwiki-20150112-400-r100-10576.txt"
    file_path = "../data/knock81.100.txt"
    line_num = 284434 # 読み込むファイルの行数 (wc -l ../data/knock81.100.txt)
    main(file_path, line_num)
