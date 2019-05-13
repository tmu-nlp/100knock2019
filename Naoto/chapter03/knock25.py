'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''

import re


def template_extract(input_file: str) -> {}:
    dic_ = {}
    start = 1
    with open(input_file) as fp:
        json_data = fp.readline()
        while start:
            basic_info = re.search("^\{\{基礎情報", json_data)
            if basic_info is not None:
                while start:
                    json_data = fp.readline()
                    finish = re.search("^\}\}", json_data)
                    if finish is not None:
                        start = 0
                        break
                    basic_info = re.search("^\|(\S+?)\s=\s(.+)", json_data)
                    if basic_info is not None:
                        dic_[basic_info.group(1)] = basic_info.group(2)
                        key = basic_info.group(1)
                    line_start = re.search("^\*+(.+)", json_data)
                    if line_start is not None:
                        dic_[key] += str(line_start.group(1))
            json_data = fp.readline()
    return dic_


if __name__ == '__main__':
    input_file = "jawiki-イギリス.json"
    dic_ = template_extract(input_file)
    print(dic_)
