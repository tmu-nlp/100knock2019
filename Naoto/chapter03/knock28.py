'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
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
