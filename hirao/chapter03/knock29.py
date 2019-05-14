import re
import requests
from IPython.display import SVG, display
from knock20 import get_text

# 正規表現...
pattern = re.compile(r'''^\|(.+?)\s = \s(.+?)(?=\n(\||\}))''',
                     re.MULTILINE | re.DOTALL | re.VERBOSE)
pattern_inner_link = re.compile(
    r'\[\[ | \]\]', re.MULTILINE | re.DOTALL | re.VERBOSE)
pattern_html = re.compile(r'^\<(.+?)\>(.+?)\<(.+?)\>')
# この段階だと、<ref></ref>が残る...
pattern_single_html = re.compile(r'<(.+?)>')
basic_info = {}
s = get_text()

for match in pattern.finditer(s):
    temp = match.group(2).replace("''''", "").replace(
        "'''", "").replace("''", "")
    temp = pattern_inner_link.sub("", temp)
    temp = pattern_html.sub("", temp)
    basic_info[match.group(1)] = pattern_single_html.sub("", temp)
## ここまで同じ

for (key, value)in basic_info.items():
    if key == "国旗画像":
        params = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "iiprop": "url",
            "titles": "File:" + value
        }
        url = "https://en.wikipedia.org/w/api.php"
        response = requests.get(url, params).json()
        # pageid = 23473560
        image_url = response['query']['pages']['23473560']['imageinfo'][0]['url']
        print(image_url)
        display(SVG(url=image_url))
