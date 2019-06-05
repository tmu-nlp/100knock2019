import joblib

def main():
    country_names = []
    word_vectors = joblib.load("word_vectors")
    word_index = joblib.load("word_index")
    with open("../chapter09/countries.txt") as f:
        for line in f:
            name = "_".join(line.rstrip().split())
            country_names.append(name)

    country_vectors = {}
    for name in country_names:
        try:
            vec = word_vectors[word_index[name]]
            country_vectors[name] = vec
        except:
            pass
    joblib.dump(country_vectors, "country_vec")

if __name__ == "__main__":
    main()