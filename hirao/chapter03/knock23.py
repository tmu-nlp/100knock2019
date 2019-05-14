import re
from knock20 import get_text

# 正規表現
# 1. (=+)で=の1回以上の繰り返し
# 2. (.+?)で任意の文字列
pattern = re.compile(r'^((=+)(.+?)(=+))')

for s in get_text().split("\n"):
    # 該当箇所を探索
    text = pattern.search(s)
    if text is not None:
        # group(0)には"==***=="や"===***==="が入ってる
        letter = text.group(0)
        i = 0
        # group(0)の=の数を数える
        while letter[i] == "=":
            i += 1
        print("{}. {}".format(i-1, letter[i:-i].replace(" ", "")))
