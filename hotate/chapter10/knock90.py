from gensim.models import word2vec


def word_2_vec(path):
    sentences = word2vec.LineSentence(path)
    model = word2vec.Word2Vec(sentences, size=300, min_count=20, window=5)
    return model


def load_word_2_vec(path):
    model = word2vec.Word2Vec.load(path)
    return model


def united_vec(model):
    print('United_States')
    print(model['United_States'])
    print()


def similarity(model):
    print('similarity')
    print(model.similarity(u'United_States', u'U.S'))
    print()


def most_similarity(model):
    print('most similarity')
    print(model.most_similar(positive=['England'], topn=10))
    print()


def calc_vec(model):
    calc = model['Spain'] - model['Madrid'] + model['Athens']
    print('Spain - Madrid + Athene')
    print(model.most_similar(positive=[calc], topn=10))


if __name__ == '__main__':
    model = word_2_vec('../chapter09/knock81.100.txt')
    model.save('word2vec')
    model = load_word_2_vec('word2vec')
    united_vec(model)
    similarity(model)
    most_similarity(model)
    calc_vec(model)