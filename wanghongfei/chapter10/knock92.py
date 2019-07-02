from gensim.models import word2vec

model = word2vec.Word2Vec.load("./chapter10/word_vec.bin")

with open("./chapter10/family_sim.txt", "w") as f:
    for line in open("./chapter10/family.txt", "r").readlines():
        try:
            w1, w2, w3, _ = line.strip().split(" ")
            w1_vec = model.wv[w1].reshape(1, -1)
            w2_vec = model.wv[w2].reshape(1, -1)
            w3_vec = model.wv[w3].reshape(1, -1)
            base = w2_vec - w1_vec + w3_vec
            results = model.wv.most_similar(positive=base)
            max_word = results[0][0]
            max_sim = results[0][1]
        except KeyError:
            max_word = "$"
            max_sim = -1
        f.write(line.strip()+" "+max_word+" "+str(max_sim)+"\n")