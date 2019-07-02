import numpy as np
from scipy.stats import rankdata

def spearman(X, Y):
    return 1.0 - (6 * sum((X - Y) ** 2) / (len(X) ** 3 - len(X)))

human = []
model = []
for line in open("./chapter10/knock94_out.txt", "r").readlines():
    word1, word2, human_score, model_socre = line.rstrip('\n').split('\t')
    human.append(human_score)
    model.append(model_socre)

human_rank = rankdata(np.array(human), method='ordinal')
model_rank = rankdata(np.array(model), method='ordinal')

print(spearman(human_rank, model_rank))