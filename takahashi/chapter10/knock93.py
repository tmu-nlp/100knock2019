
"""
93. アナロジータスクの正解率の計算

92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
"""

def accuracy_score(filename: str):
    # 正解した数 / total
    correct, total = 0, 0
    for line in open(filename, "r", encoding="utf-8"):
        tokens = line.strip().split()
        if tokens[3] == tokens[4]:
            correct += 1
        total += 1
    return correct / total


def main():
    file_w2v_faiss = "./results/faiss.w2v.out.txt"
    file_w2v = "./results/knock92.w2v.output.txt"
    file_ppmi_faiss = "./results/faiss.ppmi.out.txt"
    file_ppmi = "./results/knock92.ppmi.output.txt"

    print(f"knock 92 (Brute-force search) : {accuracy_score(file_w2v)*100:.4f} %")
    print(f"knock 85 (Brute-force search) : {accuracy_score(file_ppmi)*100:.4f} %")
    print(f"knock 92 (faiss) : {accuracy_score(file_w2v_faiss)*100:.4f} %")
    print(f"knock 85 (faiss) : {accuracy_score(file_ppmi_faiss)*100:.4f} %")

if __name__ == "__main__":
    main()

"""
knock 92 (Brute-force search) : 11.0672 %
knock 85 (Brute-force search) : 2.1739 %
knock 92 (faiss) : 2.3715 %
knock 85 (faiss) : 0.0000 %
"""