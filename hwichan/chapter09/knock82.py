import random


def main():
    with open('out_rename.txt', 'r') as input_file, \
         open('context.txt', 'w') as out_file:
        for line in input_file:
            words = line.strip().split(' ')
            for i, word in enumerate(words):
                d = random.randint(1, 5)  # 文脈幅
                # i - d: 前, i + d + 1: 後
                for j in range(max(i - d, 0), min(i + d + 1, len(words))):
                    if j == i:  # 単語と文脈幅の値が同じ
                        continue
                    print(f'{word}\t{words[j]}', file=out_file)


if __name__ == "__main__":
    main()
