#73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，
# 重みの低い素性トップ10を確認せよ

import joblib

logr = joblib.load("logr_model")
name = joblib.load("tfidf_name")

sorted_logr = sorted(list(zip(logr.coef_.flatten(), name)))

print("Worst 10")
for weight, name in sorted_logr[:10]:
    print(f"{weight:.5}\t{name}")
print("\nBest 10")
for weight, name in sorted_logr[-10:][::-1]:
    print(f"{weight:.5}\t{name}")