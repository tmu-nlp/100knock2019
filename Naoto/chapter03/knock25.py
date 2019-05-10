'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''

import re


def template_extract(input_file: str) -> {}:
    dic_ = {}
    status = 1
    with open(input_file) as fp:
        json_data = fp.readline()
        while status:
            start = re.search("^{{基礎情報", json_data)
            if start is not None:
                while status:
                    json_data = fp.readline()
                    end = re.search("^}}", json_data)
                    if end is not None:
                        status = 0
                        break
                    template = re.search("^\|(\S*) = (.*)", json_data)
                    if template is not None:
                        dic_[template.group(1)] = template.group(2)
            json_data = fp.readline()
    return dic_


if __name__ == '__main__':
    input_file = "jawiki-イギリス.json"
    dic_ = template_extract(input_file)
    print(dic_)
