import joblib
logr_model = joblib.load("logr_model")
names = joblib.load("tfidf_name")
ranking = sorted(list(zip(logr_model.coef_.flatten(), names)))

print("Worst 10")
for weight, name in ranking[:10]:
    print(f"{weight:.5}\t{name}")
print("\nBest 10")
for weight, name in ranking[-10:][::-1]:
    print(f"{weight:.5}\t{name}")