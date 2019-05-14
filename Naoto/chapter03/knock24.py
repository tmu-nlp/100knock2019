'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''

import re


def file_reference_extract(file_name: str) -> {}:
    list_ = []
    with open(file_name, 'r') as fp:
        json_data = fp.readline()
        while json_data:
            media_file = re.search("\[\[(ファイル|File):(.+?)\|thumb\S+", json_data)
            if media_file is not None:
                list_.append(media_file.group(2))
            json_data = fp.readline()
    return list_


if __name__ == "__main__":
    list_ = file_reference_extract("jawiki-イギリス.json")
    print(list_)