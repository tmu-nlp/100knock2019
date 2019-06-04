"""
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．
しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，
スペースをアンダーバーに置換せよ．
例えば，
  - "United States"は"United_States"，
  - "Isle of Man"は"Isle_of_Man"になるはずである．
"""

# contry list (JSON format)
# https://gist.github.com/keeguon/2310008#gistcomment-1661046

import json
from tqdm import tqdm
from typing import List, Generator
from knock80 import file_reader


# JSON ファイルから 2 語以上からなる国名を読み込む
def make_country_list(filename: str) -> List[str]:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [d["name"] for d in data if len(d["name"]) > 1]


# 文に国名が含まれていたら空白を _ に置き換えた文字列に置き換える
def concat_country_name(sentence: str, countries: List[str]) -> str:
    for country in countries:
        sentence = sentence.replace(country, country.replace(" ", "_"))
    return sentence


def main(line_num: int) -> None:
    country_file_path = "../data/country.json"
    countries = make_country_list(country_file_path)

    output_file_path = "./results/knock81.output"
    line = file_reader("./results/knock80.output")
    with open(output_file_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(line_num)):
            f.write(concat_country_name(line.__next__(), countries))


if __name__ == "__main__":
    line_num = 252693 # wc -l ./results/knock80.output
    main(line_num)

