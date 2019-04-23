import re
from knock20 import get_json
# 正規表現...
pattern = re.compile(r'''^\|(.+?)\s = \s(.+?)(?=\n(\||\}))''',
                     re.MULTILINE | re.DOTALL | re.VERBOSE)
pattern_inner_link = re.compile(r'\[\[ | \]\]', re.VERBOSE)
pattern_html = re.compile(r'^\<(.+?)\>(.+?)\<(.+?)\>')
pattern_clean = re.compile(r'\[(.+?)\]')
# この段階だと、<ref></ref>が残る...
pattern_single_html = re.compile(r'<(.+?)>')
basic_info = {}
s = get_json()

for match in pattern.finditer(s):
    temp = match.group(2).replace("''''", "").replace(
        "'''", "").replace("''", "")
    temp = pattern_inner_link.sub("", temp)
    temp = pattern_html.sub("", temp)
    temp = pattern_clean.sub("", temp)
    basic_info[match.group(1)] = pattern_single_html.sub("", temp)

for (key, value)in basic_info.items():
    print("{}: {}".format(key, value))
