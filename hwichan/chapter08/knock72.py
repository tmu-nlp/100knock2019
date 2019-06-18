from knock71 import is_stopwords
import re
import snowballstemmer
from collections import Counter


def main():
    stemmer = snowballstemmer.stemmer('english')  # stemmingモジュール読み込み
    features = []
    with open('sentiment.txt', 'r', encoding='latin-1') as f:
        for line in f:
            line = line.strip().split('\t')
            for word in line[1].split(' '):
                # ストップワードと1文字(.,;など)の場合コンティニュー
                if is_stopwords(word) or len(word) == 1:
                    continue

                # featuresに各単語をステミング処理をしてappend
                features.append(stemmer.stemWord(word))

    features_count = Counter(features) # key:word,value:wordの出現数 でdictを作成

    # 出現数が５以下のものは素性から削除
    features = [key for key, value in features_count.items() if value >= 6]

    with open('features.txt', 'w', encoding='latin-1') as f:
        f.write('\n'.join(features))


if __name__ == "__main__":
    main()
