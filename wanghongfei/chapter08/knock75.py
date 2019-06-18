import pickle

with open('./chapter08/model', 'rb') as f:
    model = pickle.load(f)
with open('./chapter08/vocab', 'rb') as f:
    vocab = pickle.load(f)
# descending sort
weight = []
for i, j in enumerate(model.coef_.tolist()[0]):
    weight.append((i, j))
weight_des = sorted(weight, key=lambda x: x[1])
# top10
print('top10:\n')
for i in weight_des[:10]:
    print(round(i[1], 3), " ", vocab[i[0]])
# last10
print('last:10\n')
for i in weight_des[:-10:-1]:
    print(round(i[1], 3), " ", vocab[i[0]])