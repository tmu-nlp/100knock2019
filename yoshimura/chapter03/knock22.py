'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''
import re

# [[Category:ヘルプ|はやみひよう]]
pattern = re.compile(r'^\[\[Category:(.+?)(?:\|.+)?\]\]$')

with open('Briten.txt', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            print(match.group(1))

# 繰り返しの後に?をつけると最小マッチ
# ()でグループ化
# (?:)で取り出さないグループ化