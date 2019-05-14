'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''
import re

# [[Category:ヘルプ|はやみひよう]]
pattern = re.compile(r'^\[\[Category:.+?\]\]$')

with open('Briten.txt', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            print(match.group(0))

# 同じ文字の繰り返し
# * 0回以上
# + 1回以上
# ? 0 or 1回