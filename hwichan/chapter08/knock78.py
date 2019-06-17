from knock76 import create_model
from knock77 import score
from sklearn.model_selection import cross_validate
import numpy as np


def main():
    labels, features, model = create_model('sentiment.txt')

    scoring = ["accuracy", "precision", "recall", "f1"]

    scores = cross_validate(model, features, labels, scoring=scoring, cv=5)
    '''
     scores = {'fit_time': array([1.56330824, 1.61080265, 1.47966075, 1.50063205, 1.50186753]),
               'test_precision': [...]
               'test_accuracy': [...]
               ....}
    '''

    print(f"正解率 = {np.mean(scores['test_accuracy'])}")
    print(f"適合率 = {np.mean(scores['test_precision'])}")
    print(f"再現率 = {np.mean(scores['test_recall'])}")
    print(f"F1 = {np.mean(scores['test_f1'])}")


if __name__ == "__main__":
    main()

# 正解率 = 0.7590496754942316
# 適合率 = 0.760246367507642
# 再現率 = 0.7568925165857526
# F1 = 0.7585215500971925
