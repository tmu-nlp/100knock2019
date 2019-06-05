from sklearn.cluster import KMeans
import joblib

def main():
    X = []
    keys = []
    country_vec = joblib.load("country_vec")
    for key, vector in country_vec.items():
        keys.append(key)
        X.append(vector)
    pred = KMeans(n_clusters=5).fit_predict(X)
    for key, cluster in zip(keys, pred):
        print(f"{key} {cluster}")

if __name__ == "__main__":
    main()