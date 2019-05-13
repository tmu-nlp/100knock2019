'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
'''
import re
import pprint

from knock25 import template_extract
from knock26 import Highlight_markup_removal
from knock27 import inner_link_removal


def MediaWiki_markup_removal(dic_: {}) -> {}:
    for k, v in dic_.items():
        dic_[k] = re.sub("\[.+\]", "", v)
        dic_[k] = re.sub("<.+?>", "", dic_[k])
        # dic_[k] = re.sub("", "", dic_[k])
        # dic_[k] = re.sub("", "", dic_[k])
        # dic_[k] = re.sub("", "", dic_[k])
    return dic_


if __name__ == "__main__":
    input_file = "jawiki-イギリス.json"
    dic_ = template_extract(input_file)
    dic_markup_removal = Highlight_markup_removal(dic_)
    dic_inner_link_removal = inner_link_removal(dic_markup_removal)
    dic_media_wiki_marckup_removal = MediaWiki_markup_removal(dic_inner_link_removal)
    pprint.pprint(dic_media_wiki_marckup_removal)