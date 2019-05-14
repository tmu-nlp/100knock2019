import re
from knock20 import get_text

# 正規表現
# 1. [[File:で始まるもの
# 2. (.+?)で任意の文字列
# 3. (\|.+)?で|の任意の回数の繰り返し
# 4. ]]で閉じる
# Categoryとほぼ同じ
pattern = re.compile(r'^\[\[File:(.+?)(\|.+)?\]\]$')

for s in get_text().split("\n"):
    text = pattern.search(s)
    if text is not None:
        print(text.group(0))
