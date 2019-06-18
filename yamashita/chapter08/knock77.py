from sklearn.externals import joblib
from sklearn.model_selection import cross_validate
from tqdm import tqdm


def main():
    with open('result_knock76.txt') as i_file:
        tp = tn = fp = fn = 0
        for line in tqdm(i_file):
            label, pre, _ = line.rstrip().split('\t')
            label = int(label)
            pre = int(pre)

            if label == 1 and pre == 1:
                tp += 1
            elif label == -1 and pre == 1:
                fp += 1
            elif label == 1 and pre == -1:
                fn += 1
            else:
                tn += 1

        accuracy_ = (tp + tn) / (tp + tn + fp + fn)
        precision_ = tp / (tp + fp)
        recall_ = tp / (tp + fn)
        f1_ = (2*precision_*recall_) / (precision_ + recall_)

        print(f'正解率 : {accuracy_}')
        print(f'正例に関する適合率 : {precision_}')
        print(f'正例に関する再現率 : {recall_}')
        print(f'正例に関するF1スコア : {f1_}')


if __name__ == '__main__':
    main()
