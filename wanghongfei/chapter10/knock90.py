from gensim.models import word2vec

model = word2vec.Word2Vec.load("./chapter10/word_vec.bin")

print(model['United_States'])

print(model.similarity('United_States', 'U.S.'))

sim_England = model.most_similar('England', topn=10)
print('\n'.join(map(lambda x: '{}'.format(x), sim_England)))

sim_Answer = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
print('\n'.join(map(lambda x: '{}'.format(x), sim_Answer)))