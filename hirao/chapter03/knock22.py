import re
from knock20 import get_text

# 正規表現
# 1. 行頭が"[[Category:"で始まる
# 2. (.+?)は任意の文字列を表す
# 3. (\|.+)?で"|***"となる部分を0以上繰り返す
# 4. 最後に]]で閉じられる
pattern = re.compile(r'^\[\[Category:(.+?)(\|.+)?\]\]$')

for s in get_text().split("\n"):
    # 各行で該当箇所を探す
    text = pattern.search(s)
    # 該当箇所が見つかった場合
    if text is not None:
        # 1つ目(上の説明で言う2に該当する部分)を抜き出す
        print(text.group(1))
