def cos_accuracy(filename: str) -> float:
    total = 0
    correct = 0
    with open(filename, 'r') as f:
        for line in f:
            cols = line.strip().split(' ')
            total += 1
            if cols[3] == cols[5]:
                correct += 1

    return correct, total, correct / total


def main():
    correct92, total92, accuracy92 = cos_accuracy('family_cos92.txt')
    correct85, total85, accuracy85 = cos_accuracy('family_cos85.txt')
    print(f'accuracy92 = {accuracy92*100}% ({correct92}/{total92})')
    print(f'accuracy85 = {accuracy85*100}% ({correct85}/{total85})')


if __name__ == "__main__":
    main()

# accuracy92 = 8.893280632411066% (45/506)
# accuracy85 = 1.7786561264822136% (9/506)

