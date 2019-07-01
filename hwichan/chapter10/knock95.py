import numpy as np


def make_list(filename: str) -> list:
    answer = []
    cos_sim = []
    with open(filename, 'r') as f:
        for line in f:
            cols = line.strip().split('\t')
            answer.append(float(cols[2]))
            cos_sim.append(float(cols[3]))

        # argsort: listを昇順でソートしindexを格納
        answer = np.argsort(answer)
        cos_sim = np.argsort(cos_sim)

        answer_rank = [0] * len(answer)
        cos_sim_rank = [0] * len(cos_sim)

        for i in range(len(answer)):
            answer_rank[answer[i]] = i
            cos_sim_rank[cos_sim[i]] = i

        return answer_rank, cos_sim_rank


def spearman(answer_rank: list, cos_sim_rank: list) -> float:
    x = 0
    for i, j in zip(answer_rank, cos_sim_rank):
        x += (i - j) ** 2

    return 1 - 6 * x / (len(answer_rank) * (len(answer_rank)**2 - 1))


def main():
    answer_rank94, cos_sim_rank94 = make_list('combined_knock94.txt')
    answer_rank85, cos_sim_rank85 = make_list('combined_knock85.txt')

    print(f'knock94 {spearman(answer_rank94, cos_sim_rank94)}')
    print(f'knock85 {spearman(answer_rank85, cos_sim_rank85)}')


if __name__ == "__main__":
    main()


# knock94 0.5120789447264695
# knock85 0.21641815475540926
