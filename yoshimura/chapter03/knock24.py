'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''
import re

# [[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
pattern = re.compile(r'\[\[(?:ファイル|File):(?P<file_name>.+?)\|(.+)\]\]')

with open('Briten.txt', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            print(match.group('file_name'))

# (?P<name> )で名前をつけられる