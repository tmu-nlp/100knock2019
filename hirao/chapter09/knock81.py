import bz2
from collections import defaultdict
from tqdm import tqdm

class Country:
    def __init__(self):
        self.country = defaultdict(lambda: [])
        # 先頭の文字で辞書を作る
        for line in open("countries.txt"):
            country_name = line.split()
            head = country_name[0]
            name_len = len(country_name)
            self.country[head].append([name_len, country_name])
        # sort
        for head in self.country.keys():
            self.country[head] = sorted(self.country[head], key=lambda x: x[0], reverse=True)

    def preprocess(self, sentence):
        tokens = []
        for word in sentence.rstrip().split():
            token = word.strip('''.,!?;:()[]'"''')
            if token == "":
                continue
            tokens.append(token)
        return " ".join(tokens)

    def process_country(self, sentence):
        sentence = self.preprocess(sentence)
        tokens = []
        sentence = sentence.split()
        sentence_len = len(sentence)
        i = 0
        # 文末まで
        while i < sentence_len:
            token = sentence[i]
            # 先頭文字が一致する場合
            if token in self.country.keys():
                for l in self.country[token]:
                    # 一つ目は長さ
                    size = l[0]
                    # 国名の単語のリスト
                    name_l = l[1]
                    if i + size < sentence_len and sentence[i:i+size] == name_l:
                        # アンダースコア区切り
                        token = "_".join(name_l)
                        # 読み込んだ単語文飛ばす
                        i += size - 1
                        # 最長一致で一致したら終わり
                        break
            tokens.append(token)
            i += 1
        return " ".join(tokens)

def main():
    c = Country()
    file_name = "enwiki-20150112-400-r100-10576.txt.bz2"
    with open("knock81.txt", "w") as fw:
        for sentence in bz2.open(file_name, mode="rb"):
            fw.write(c.process_country(sentence.decode('utf8')) + "\n")

if __name__ == "__main__":
    main()