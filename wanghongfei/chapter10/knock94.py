from gensim.models import word2vec

model = word2vec.Word2Vec.load("./chapter10/word_vec.bin")
with open("./chapter10/knock94_out.txt", "w") as f:
    for line in open("./chapter10/combined.tab", "r").readlines():
        words = line.strip().split()
        try:
            sim = model.similarity(words[0], words[1])
        except:
            sim = 0
        print(line.strip()+"\t"+str(sim), file=f)
