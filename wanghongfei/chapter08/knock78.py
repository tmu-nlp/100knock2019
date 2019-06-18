import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

with open('./chapter08/feature', 'rb') as f1, open('./chapter08/sentiment', 'rb') as f2:
    sentence = pickle.load(f1)
    label = pickle.load(f2)

sentence_train, sentence_test, label_train, label_test = train_test_split(sentence, label, test_size=0.2)
model = LogisticRegression(random_state=0).fit(sentence_train, label_train)
test_predict = model.predict(sentence_test)
print(classification_report(label_test, test_predict))

