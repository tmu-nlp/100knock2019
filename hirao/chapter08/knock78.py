from sklearn.model_selection import cross_validate
from sklearn.model_selection import StratifiedKFold
import joblib
from statistics import mean

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=16)

model = joblib.load("logr_model")
feature = joblib.load("tfidf_feature")
sentiments = joblib.load("tfidf_sentiment")

metrics = ['accuracy', 'precision', 'recall', 'f1']
scores = cross_validate(model, feature, sentiments, cv=skf, scoring=metrics)
accuracy = mean(scores['test_accuracy'])
precision = mean(scores['test_precision'])
recall = mean(scores['test_recall'])
f1 = mean(scores['test_f1'])
print("Result of 5-fold CV")
print(f"Accuracy: {accuracy:.3}\nPrecision: {precision:.3}\nRecall: {recall:.3}\nF1-score: {f1:.3}")