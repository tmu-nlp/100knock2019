from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
from knock76 import predict

_, _, predict_y = predict()
test_y = joblib.load('tfidf_sentiment')
test_y = np.array(test_y)
for i in range(len(test_y)):
    if test_y[i] < 0:
        test_y[i] = 0

# fpr, tpr, thresholds = metrics.roc_curve(test_y, predict_y)
precision, recall, thresholds = metrics.precision_recall_curve(test_y, predict_y)

# auc = metrics.auc(fpr, tpr)
# plt.plot(fpr, tpr, label='ROC curve (area = %.2f)'%auc)

plt.plot(precision, recall)
plt.title('Precision-recall-curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.grid(True)