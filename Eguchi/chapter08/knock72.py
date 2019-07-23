#極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
#素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
import collections
import codecs
from nltk import stem
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import joblib

def reg_stop_word():
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
    stop_word_list = []
    for words in stop_words:
        for word in words.split(","):
            stop_word_list.append(word)

    return stop_word_list


def remove_stopwprd(sentence):
    stopword_list = reg_stop_word()
    output = ""
    stemmer = stem.PorterStemmer()
    
    for word in sentence.lower().split():
        word = stemmer.stem(word)
        
        if word in stopword_list:
            continue
        output += word + " "
    return output




def extract():
    input_path = r"C:\Users\Koya\Documents\Lab\sentiment.txt"
    
    fencoding = "cp1252"
    label = list()
    corpus =list()
    
    with codecs.open(input_path, "r", fencoding) as f:
        for line in f:
            label.append(line[:2])
            line = line[3:]
            corpus.append(remove_stopwprd(line))
        
    
    vectorizer = TfidfVectorizer()
    feature = vectorizer.fit_transform(corpus).toarray()
    sentiment = np.array(label)
    joblib.dump(feature, 'tfidf_feature')
    joblib.dump(sentiment, 'tfidf_sentiment')
    joblib.dump(vectorizer.vocabulary_, 'tfidf_vocab')
    joblib.dump(vectorizer.get_feature_names(), 'tfidf_name')

def count_f():
    input_path = r"C:\Users\Koya\Documents\Lab\sentiment.txt"
    
    fencoding = "cp1252"
    label = list()
    corpus =list()
    
    with codecs.open(input_path, "r", fencoding) as f:
        for line in f:
            label.append(line[:2])
            line = line[3:]
            corpus.append(remove_stopwprd(line))
    
    count_vectorizer = TfidfVectorizer()
    feature = count_vectorizer.fit_transform(corpus).toarray()
    sentiment = np.array(label)
    joblib.dump(feature, 'count_feature')
    joblib.dump(sentiment, 'count_sentiment')
    joblib.dump(count_vectorizer.vocabulary_, 'count_vocab')
    joblib.dump(count_vectorizer.get_feature_names(), 'count_name')

extract()
count_f()