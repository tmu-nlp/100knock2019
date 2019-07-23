#73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
# その予測確率を計算するプログラムを実装せよ．
import collections

from nltk import stem
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib



def input_data():
    input_path = r"C:\Users\Koya\Documents\Lab\sentiment.txt"
    f = open(input_path, encoding='latin-1')
    for _ in range(2):
        next(f)
    sentence = f.readline()
    sentence = sentence.strip()[3:]
    print("Input sentence\n", sentence)
    feature = remove_stopwprd(sentence)
    return feature

def make_vec(feature):
    model = joblib.load('logr_model')
    vocab = joblib.load('tfidf_vocab')
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    feature_vec = vectorizer.fit_transform([feature]).toarray()
    predict = model.predict(feature_vec)[0]
    probability = model.predict_proba(feature_vec).flatten()
    print(f"Predict result: {predict}")
    print(f"Probability of result\n-1: {probability[0]:.2}%\n+1: {probability[1]:.2}%")




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


fe = input_data()
make_vec(fe)
