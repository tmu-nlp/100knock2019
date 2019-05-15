from itertools import islice
from typing import Tuple, List, Optional

import numpy as np
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.utils import shuffle
from sklearn.utils.deprecation import DeprecationDict


class Classifier:
    def __init__(self,
                 vectorizer: TfidfVectorizer = TfidfVectorizer(),
                 model: LogisticRegression = LogisticRegression(),
                 sentence_list: Optional[List[str]] = None,
                 label_list: Optional[List[str]] = None,
                 data_x: Optional[np.ndarray] = None,
                 data_y: Optional[np.ndarray] = None) -> None:
        self.vectorizer = vectorizer
        self.model = model
        self.sentence_list = sentence_list
        self.label_list = label_list
        self.data_x = data_x
        self.data_y = data_y
        self.check_data()

    def create_data_x(self):
        self.data_x = self.vectorizer.transform(self.sentence_list)

    def create_data_y(self):
        self.data_y = np.array(self.label_list, dtype=int)

    def check_data(self):
        if not self.data_x:
            self.create_data_x()
        if not self.data_y:
            self.create_data_y()

    def train_model(self):
        self.data_x, self.data_y = shuffle(self.data_x, self.data_y)
        self.model.fit(self.data_x, self.data_y)
        joblib.dump(self.model, 'model.pkl')

    def predict(self, stop: int = 20) -> List[Tuple[str, str, List[float], str]]:
        pred_list = list()
        for vec, sentence, gold in islice(zip(self.data_x, self.sentence_list, self.label_list), stop):
            pred = self.model.predict(vec)[0]
            pred_label = pred_to_label(pred)
            prob = self.model.predict_proba(vec).tolist()[0]
            pred_list.append((sentence, pred_label, prob, gold))
        return pred_list

    def weight_rank(self) -> List[Tuple[float, str]]:
        word = self.vectorizer.get_feature_names()
        weight = self.model.coef_[0].tolist()
        pair = list(zip(weight, word))
        pair.sort()
        return pair

    def accuracy(self) -> Tuple[np.ndarray, np.ndarray]:
        label_true, label_pred = self.data_y, self.model.predict(self.data_x)
        return label_true, label_pred

    def kfold(self, k: int = 5) -> DeprecationDict:
        scoring = {
            'accuracy': 'accuracy',
            "precision": "precision",
            "recall": "recall",
            "f1": "f1"
        }
        skf = StratifiedKFold(n_splits=k, shuffle=True)
        scores = cross_validate(self.model, self.data_x, self.data_y, cv=skf, scoring=scoring)
        return scores

    def precision_recall(self) -> Tuple[np.ndarray, np.ndarray]:
        precision, recall, threshold = precision_recall_curve(self.data_y, self.model.predict_proba(self.data_x)[:, 1],
                                                              pos_label=1)
        return precision, recall


def pred_to_label(pred: np.int64) -> str:
    return '+1' if pred == 1 else '-1'


def main():
    vectorizer = joblib.load('vectorizer.pkl')
    label_list = joblib.load('label.pkl')
    sentence_list = joblib.load('sentences.pkl')
    model = Classifier(vectorizer=vectorizer, sentence_list=sentence_list, label_list=label_list)
    model.train_model()


if __name__ == '__main__':
    main()
