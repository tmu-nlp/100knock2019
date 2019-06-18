from sklearn.metrics import classification_report
import pickle

with open('./chapter08/model', 'rb') as f1, open('./chapter08/feature', 'rb') as f2:
    model = pickle.load(f1)
    feature = pickle.load(f2)
with open('./chapter08/sentiment', 'rb') as f:
    label = pickle.load(f)
predict = model.predict(feature)

print(classification_report(label, predict))