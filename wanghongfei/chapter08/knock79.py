import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import precision_recall_curve
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

with open('./chapter08/feature', 'rb') as f1, open('./chapter08/sentiment', 'rb') as f2:
    sentence = pickle.load(f1)
    label = pickle.load(f2)

sentence_train, sentence_test, label_train, label_test = train_test_split(sentence, label, test_size=0.2)
model = LogisticRegression(random_state=0).fit(sentence_train, label_train)
test_predict = model.predict(sentence_test)
prob = model.predict_proba(sentence_test)[:, 1]

lb = preprocessing.LabelBinarizer()
lb.fit(label_test)
label_2 = lb.transform(label_test).ravel()
# precision_recall_curve(y_true, probas_pred)
precsion, recall, threshold = precision_recall_curve(label_2, prob)
plt.plot(precsion, recall)
plt.xlabel('precision')
plt.ylabel('recall')
plt.show()