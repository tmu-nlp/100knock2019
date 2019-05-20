'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
'''
import re

# == Level == 2~5まで
pattern = re.compile(r'^(={2,5})(.+)(\1)$')

with open('Briten.txt', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            s = match.group(0)
            level = int(sum(c == '=' for c in s)/2 - 1)
            print(match.group(2).strip(), level)


# \数字で前に出たグループを指定できる
# {m,n}でm回以上n回以下の繰り返し