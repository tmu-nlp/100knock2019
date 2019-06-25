from tqdm import tqdm
import random


def get_context(current_id, words):
    def lambda_func(x): return max(0, min(len(words), x))
    d = random.randint(1, 5)
    left = words[lambda_func(current_id-d):current_id]
    right = words[lambda_func(current_id+1):current_id+d+1]
    return left + right


def main():
    with open('result_knock81.txt', 'r', encoding='utf-8') as i_file:
        with open('result_knock82.txt', 'w', encoding='utf-8') as w_file:
            for line in tqdm(i_file):
                words = line.strip().split()
                for i in range(len(words)):
                    # d = random.randint(1, 5)
                    # left = words[max(i-d, 0):i]
                    # right = words[min(i+1, len(words)):i+d+1]
                    # if ' '.join(left + right) == '':
                    #     continue
                    context = get_context(i, words)
                    if not context:
                        continue
                    print(f'{words[i]}\t{" ".join(context)}', file=w_file)


if __name__ == '__main__':
    main()
