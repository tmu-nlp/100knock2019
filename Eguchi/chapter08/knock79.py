#ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．

"""

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

def detect(sentence):
    stop_list = reg_stop_word()
    sentence = sentence.lower()
    for word in sentence.split():
        return word in stop_list



def extract_model():
    input_path = r"C:\Users\Koya\Documents\Lab\sentiment.txt"
    
    fencoding = "cp1252"
    label_list = list()
    without_label_list = list()
    line_list = list()
    


    with codecs.open(input_path, "r", fencoding) as f:
        for line in f:
            label = line[:2]
            without_label = line[3:]
            for word in without_label.split(" "):
                if detect(word) :
                    continue
                word= stemmer.stem(word)
                line_list.append(word)
                without_label_list.append(without_label)    
                label_list.append(label)
    
    return line_list, label_list


def make_model():

    output, label_list = extract_model()
    
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(output).toarray()
    model = LogisticRegression().fit(features, label_list)
    print("type of vec = %s" %vectorizer)
    return vectorizer, model

def predict():
    vect, model = extract_model()

    key = input("レビュー----→")
    sentence = []
    for word in key.split(" "):
        if detect(word):
            continue
        sentence.append(stemmer.stem(word))
    sentences = " ".join(sentence)
    
    vectorizer = TfidfVectorizer(vocabulary=vect.vocabulary_)
    features = vectorizer.fit_transform(sentences).toarray()

    print(features)

    print(f'{model.predict(features)[0]} : {max(model.predict_proba(features)[0])}')
predict()
"""