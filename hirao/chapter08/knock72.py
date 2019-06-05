import time
import pickle
import snowballstemmer
import joblib
# sklearn.external.joblibが非推奨に？
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np

class FeatureEnginnering:
    def __init__(self):
        self.stemmer = snowballstemmer.stemmer('english')
        self.stop_words = []
        stop_words = [
            "i,me,my,myself,we,our,ours,ourselves,you,your,yours",
            "yourself,yourselves,he,him,his,himself,she,her,hers",
            "herself,it,its,itself,they,them,their,theirs,themselves",
            "what,which,who,whom,this,that,these,those,am,is,are,was",
            "were,be,been,being,have,has,had,having,do,does,did",
            "doing,a,an,the,and,but,if,or,because,as,until,while",
            "of,at,by,for,with,about,against,between,into,through",
            "during,before,after,above,below,to,from,up,down,in,out",
            "on,off,over,under,again,further,then,once,here,there",
            "when,where,why,how,all,any,both,each,few,more,most",
            "other,some,such,no,nor,not,only,own,same,so,than,too",
            "very,can,will,just,don,should,now"
        ]
        for row in [words.split(",") for words in stop_words]:
            self.stop_words.extend(row)

    def remove_stop_word(self, sentence):
        '''
        入力した文のストップワードを除去し、ステミングした文を出す
        '''
        output = ""
        for word in sentence.lower().split():
            word = self.stemmer.stemWord(word)
            if word in self.stop_words:
                continue
            output += word + " "
        return output.strip()

    def tf_idf_feature(self, file_name):
        '''
        入力ファイル
        先頭に-1か+1が付き、半角スペースのあとに文章が入力されている形式
        '''
        labels = []
        corpus = []

        for line in open(file_name, encoding='utf8'):
            labels.append(int(line[:2]))
            sentence = line.rstrip()[3:]
            corpus.append(self.remove_stop_word(sentence))

        tf_idf_vectorizer = TfidfVectorizer()
        feature = tf_idf_vectorizer.fit_transform(corpus).toarray()
        sentiment = np.array(labels)
        # pickleよりjoblib.dumpの方が早い？
        # joblib.dump:2.585sec]
        # pickle.dump:6.703[sec]
        # np.savez: 2.552[sec]

        joblib.dump(feature, 'tfidf_feature')
        joblib.dump(sentiment, 'tfidf_sentiment')
        joblib.dump(tf_idf_vectorizer.vocabulary_, 'tfidf_vocab')
        joblib.dump(tf_idf_vectorizer.get_feature_names(), 'tfidf_name')

    def count_feature(self, file_name):
        corpus = []
        labels = []

        for line in open(file_name, encoding='utf8'):
            labels.append(int(line[:2]))
            sentence = line.rstrip()[3:]
            corpus.append(self.remove_stop_word(sentence))

        count_vectorizer = CountVectorizer()
        feature = count_vectorizer.fit_transform(corpus).toarray()
        sentiment = np.array(labels)
        # pickleよりjoblib.dumpの方が早い？
        joblib.dump(feature, 'count_feature')
        joblib.dump(sentiment, 'count_sentiment')
        joblib.dump(count_vectorizer.vocabulary_, 'count_vocab')
        joblib.dump(count_vectorizer.get_feature_names(), 'count_name')

if __name__ == "__main__":
    fe = FeatureEnginnering()
    fe.tf_idf_feature("sentiment.txt")
    fe.count_feature("sentiment.txt")