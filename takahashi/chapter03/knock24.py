# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

from knock20 import get_country_data
from typing import List
import re

# [[File:Battle of Waterloo 1815.PNG|thumb|left|[[ワーテルローの戦い]]
#   -> Battle of Waterloo 1815.PNG
# [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]
#   -> Royal Coat of Arms of the United Kingdom.svg
def get_media_file(target: str) -> List[str]:
    pattern = r"""
        \[\[             # [[
        (?:File|ファイル) # 非キャプチャ, File または ファイル に一致
        :                # :
        (.+?)            # キャプチャ対象のリンク
        \|               # | 
        (?:.+)           # | 以降の非キャプチャ対象
        \]\]             # ]]
        """
    regex = re.compile(pattern, re.MULTILINE | re.VERBOSE)
    return regex.findall(target)


if __name__ == "__main__":
    target = get_country_data("イギリス")
    for media in get_media_file(target):
        print(media)
