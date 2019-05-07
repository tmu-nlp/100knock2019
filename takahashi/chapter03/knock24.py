# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

from knock20 import get_country_data
import re

def extract_media_file(target: str) -> str:
    # [[File: ... ]] の行を抽出する
    regex = r"^\[\[File:.+\]\]$"
    matches = re.findall(regex, target, re.MULTILINE)

    # メディアファイル名以外の文字を除去する
    result = []
    for match in matches:
        res = re.sub("\[\[File:", "", match.split("|")[0])
        result.append(res)   
    return result

if __name__ == "__main__":
    target = get_country_data("イギリス")
    for media in extract_media_file(target):
        print(media)