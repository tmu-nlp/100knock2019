'''
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
'''
import re
from knock25 import template_extract
from knock26 import Highlight_markup_removal


def inner_link_removal(dic_: {}) -> {}:
    for k, v in dic_.items():
        inner_link = re.findall("\[\[(.+?)\]\]", v)
        if len(inner_link) != 0:
            dic_[k] = re.sub("\[\[([^\[\]]+?)#([^\[\]]+?)\
                \|([^\[\]]+?)\]\]", r"\3", v)
            dic_[k] = re.sub("\[\[([^\[\]]+?)\|([^\[\]]+?)\
                \]\]", r"\2", dic_[k])
            dic_[k] = re.sub("\[\[([^\[\]]+?)\]\]", r"\1", dic_[k])
    return dic_


if __name__ == "__main__":
    input_file = "jawiki-イギリス.json"
    dic_ = template_extract(input_file)
    dic_markup_removal = Highlight_markup_removal(dic_)
    dic_inner_link_removal = inner_link_removal(dic_markup_removal)
    print(dic_inner_link_removal)
