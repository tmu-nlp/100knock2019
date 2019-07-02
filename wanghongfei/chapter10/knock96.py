from gensim.models import word2vec
import pickle

countries_set = set()
for line in open('./chapter09/country.txt', 'r').readlines():
    if len(line) > 2:
        countries_set.add(line.strip().replace(" ", "_"))

model = word2vec.Word2Vec.load("./chapter10/word_vec.bin")
country_dict = {}
vec = []
index = 0
for country in countries_set:
    try:
        vec.append(model[country])
        country_dict[index] = country
        index += 1
    except KeyError:
        pass

with open('./chapter10/country_vec', 'wb') as f:
    pickle.dump(country_dict, f)
    pickle.dump(vec, f)


        