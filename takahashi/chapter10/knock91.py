"""
91. アナロジーデータの準備

単語アナロジーの評価データをダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，"family"というセクションに含まれる評価事例を抜き出してファイルに保存せよ．
"""


def main(in_file: str):
    out_file = "./results/knock91.output.txt"

    lines = []
    target_line = False
    for line in open(in_file, "r", encoding="utf-8"):
        if line.rstrip() == ": family":
            target_line = True
            continue

        if target_line and line.startswith(":"):
            break

        if target_line:
            lines.append(line)  # 改行も含めて append する

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("".join(lines))


if __name__ == "__main__":
    file_path = "../data/questions-words.txt"
    main(file_path)
