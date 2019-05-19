import re
from typing import List
SENTENCE_SIZE = 10

def load_txt(file_name: str) -> List[List[dict]]:
    '''
    input:
        一	名詞,数,*,*,*,*,一,イチ,イチ
        EOS
        EOS
            記号,空白,*,*,*,*,　,　,　
        吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
        は	助詞,係助詞,*,*,*,*,は,ハ,ワ
        猫	名詞,一般,*,*,*,*,猫,ネコ,ネコ
        で	助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
        ある	助動詞,*,*,*,五段・ラ行アル,基本形,ある,アル,アル
        。	記号,句点,*,*,*,*,。,。,。
    '''
    sentence_list = []
    word_list = []
    for line in open(file_name, encoding='utf8'):
        # EOSが来たら文の終わりなので、文ごとにリストに格納する
        if line == 'EOS\n':
            sentence_list.append(word_list)
            word_list = []
            continue
        # \tとコンマで文を分割する
        splited = re.split('[\t,]', line.strip())
        # 文頭の空白の時用のやつ
        if len(splited) == 9:
            splited.insert(0, " ")
        # 表層形、基本形、品詞、品詞細分類1を格納する
        word_params = {
            'surface': splited[0],
            'base'   : splited[7],
            'pos'    : splited[1],
            'pos1'   : splited[2],
        }
        word_list.append(word_params)
    return sentence_list

if __name__ == "__main__":
    sentence_list = load_txt("neko.txt.mecab")
    for i in range(SENTENCE_SIZE):
        for word_list in sentence_list[i]:
            print(word_list)