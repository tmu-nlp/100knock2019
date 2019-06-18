from sklearn.linear_model import LogisticRegression
import pickle

with open("./chapter08/feature", "rb") as f1, open("./chapter08/sentiment", "rb") as f2:
    x = pickle.load(f1)
    y = pickle.load(f2)
model = LogisticRegression(random_state=0).fit(x, y)
with open("./chapter08/model", "wb") as f:
    pickle.dump(model, f)



