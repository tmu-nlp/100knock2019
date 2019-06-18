import pickle

with open('./chapter08/model', 'rb') as f1, open('./chapter08/feature', 'rb') as f2:
    model = pickle.load(f1)
    feature = pickle.load(f2)
with open('./chapter08/sentiment', 'rb') as f:
    label = pickle.load(f)
label_predict = model.predict(feature)
prob = model.predict_proba(feature)
for lab, lab_pre, prob in zip(label, label_predict, prob):
    print(f'{lab}\t{lab_pre}\t{prob}')