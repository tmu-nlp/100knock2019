import re
from knock20 import get_json

pattern = re.compile(r'^((=+)(.*?)=\2)')

for s in get_json().split("\n"):
    text = pattern.search(s)
    if text is not None:
        ret = text.group(0)
        i = 0
        while ret[i] == "=":
            i += 1
        print("{}: {}".format(i-1, ret[i:-i].replace(" ", "")))
