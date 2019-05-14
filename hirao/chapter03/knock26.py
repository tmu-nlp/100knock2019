import re
from knock20 import get_text
# 正規表現...
pattern = re.compile(r'''^\|(.+?)\s = \s(.+?)(?=\n(\||\}))''',
                     re.MULTILINE | re.DOTALL | re.VERBOSE)
basic_info = {}
s = get_text()

for match in pattern.finditer(s):
    basic_info[match.group(1)] = match.group(2).replace(
        "''''", "").replace("'''", "").replace("''", "")

for (key, value)in basic_info.items():
    print("{}: {}".format(key, value))
