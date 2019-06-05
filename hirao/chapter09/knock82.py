import random
from collections import defaultdict


def main():
    with open("knock81.txt") as f, open("knock82.txt", mode="w") as fw:
        for line in f:
            words = line.split()
            sen_len = len(words)
            for i, base_word in enumerate(words):
                d = random.randint(1, 5)
                # 単語の前d単語
                for j in range(i-d, i):
                    if 0 <= j:
                        fw.write(f"{base_word}\t{words[j]}\n")
                # 単語の後d単語
                for j in range(i + 1, i + d + 1):
                    if j < sen_len:
                        fw.write(f"{base_word}\t{words[j]}\n")


if __name__ == "__main__":
    main()
