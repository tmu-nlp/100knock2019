def score(filename: str) -> float:
    tp = 0  # true-positive（真陽性）  予想 : 1 正解 : 1
    fp = 0  # false-positive（偽陽性） 予想 : 1 正解 : -1
    fn = 0  # false-negative（偽陰性） 予想 : -1 正解 : 1
    tn = 0  # true-negative（真陰性）  予想 : -1 正解 : -1

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            answer_label = line[0]
            predict_label = line[1]

            if predict_label == '1':
                if answer_label == '1':
                    tp += 1
                else:
                    fp += 1
            else:
                if answer_label == '1':
                    fn += 1
                else:
                    tn += 1

    accuracy = (tp + tn) / (tp + fp + fn + tn)  # 正解率
    precision = tp / (tp + fp)  # 正解に対する適合率 : 1と予測した中で実際に正解が1だったものの割合
    recall = tp / (tp + fn)  # 正解に対する再現率 : 正解が1だったものに対して予測も1であるものの割合
    f1 = 2 * (precision * recall) / (precision + recall)

    return accuracy, precision, recall, f1


def main():
    accuracy, precision, recall, f1 = score('result.txt')

    print(f'正解率 = {accuracy}')
    print(f'適合率 = {precision}')
    print(f'再現率 = {recall}')
    print(f'F1 = {f1}')


if __name__ == "__main__":
    main()


# 正解率 = 0.8812605514912775
# 適合率 = 0.884433516171742
# 再現率 = 0.877133746013881
# F1 = 0.8807685063100396
