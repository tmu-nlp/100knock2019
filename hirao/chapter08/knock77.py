from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from knock76 import predict
true, pred, _ = predict()
accuracy = accuracy_score(true, pred)
precision = precision_score(true, pred)
recall = recall_score(true, pred)
f1 = f1_score(true, pred)
print(f"Accuracy: {accuracy:.3}\nPrecision: {precision:.3}\nRecall: {recall:.3}\nF1-score: {f1:.3}")