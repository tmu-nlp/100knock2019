import re
from knock20 import get_json

pattern = re.compile(r'^\[\[File:(.+?)(?:\|.+)?\]\]$')

for s in get_json().split("\n"):
    text = pattern.search(s)
    if text is not None:
        ret = text.group(0)
        print(ret)
