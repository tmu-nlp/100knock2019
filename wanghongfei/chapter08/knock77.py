from sklearn.metrics import classification_report, f1_score
import pickle
from sklearn import preprocessing

with open('./chapter08/model', 'rb') as f1, open('./chapter08/feature', 'rb') as f2:
    model = pickle.load(f1)
    feature = pickle.load(f2)
with open('./chapter08/sentiment', 'rb') as f:
    label = pickle.load(f)
predict = model.predict(feature)

lb = preprocessing.LabelBinarizer()
lb.fit(label)
label_2 = lb.transform(label).ravel()
lb.fit(predict)
predict_2 = lb.transform(predict).ravel() 

print(round(f1_score(label_2, predict_2), 3))