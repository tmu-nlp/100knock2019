import re
from knock20 import get_text
# 正規表現...
pattern = re.compile(r'''^\|(.+?)\s = \s(.+?)(?=\n(\||\}))''',
                     re.MULTILINE | re.DOTALL | re.VERBOSE)
pattern_inner_link = re.compile(r'\[\[ | \]\]', re.VERBOSE)

basic_info = {}
s = get_text()

for match in pattern.finditer(s):
    temp = match.group(2).replace("''''", "").replace(
        "'''", "").replace("''", "")
    temp = pattern_inner_link.sub("", temp)
    basic_info[match.group(1)] = temp


for (key, value)in basic_info.items():
    print("{}: {}".format(key, value))
