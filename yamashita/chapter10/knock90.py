from sklearn.externals import joblib
from gensim.models import word2vec
import logging
from pprint import pprint


def knock86_89(wv):
    print(f'result knock86\n{wv["United_States"]}')

    print(f'result knock87')
    print(wv.similarity('United_States', 'U.S'))

    print('result knock88')
    pprint(wv.most_similar('England'))

    print('result knock89')
    pprint(wv.most_similar(positive=['Spain', 'Athens'], negative=['Madrid']))


def main():
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence('../chapter9/result_knock81.txt')
    model = word2vec.Word2Vec(sentences, size=100, min_count=1)
    model.wv.save('knock90.model')

    knock86_89(model.wv)


if __name__ == '__main__':
    main()
