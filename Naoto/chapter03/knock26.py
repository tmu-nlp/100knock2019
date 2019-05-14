'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去して\
    テキストに変換せよ（参考: マークアップ早見表）．
'''

from knock25 import template_extract

def Highlight_markup_removal(dic_: {}) -> {}:
    for k, v in dic_.items():
            dic_[k] = v.replace("'", "")
    return dic_

if __name__ == "__main__":
    input_file = "jawiki-イギリス.json"
    dic_ = template_extract(input_file)
    dic_removal = Highlight_markup_removal(dic_)
    print(dic_removal)