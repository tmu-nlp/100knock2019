import re
from knock20 import get_text
# 正規表現
# MULTILINE: 複数行マッチング
# DOTALL: .を改行以外のあらゆる文字と解釈する
# 1. \|(.+?) |***から始まる

pattern  = re.compile(r'^\|(.+?)\s=\s(.+?)(?=\n(\||\}))',re.MULTILINE | re.DOTALL)
basic_info = {}
s = get_text()

for match in pattern.finditer(s):
        basic_info[match.group(1)] = match.group(2)

for (key, value)in basic_info.items():
        print("{}: {}".format(key, value))
