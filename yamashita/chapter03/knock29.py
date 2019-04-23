import sys
import re
import requests

pattern = re.compile(r'^\|(.+?)\s=\s(.+?)(?=\n(\||\}))', re.MULTILINE | re.DOTALL)
pattern_emphasis = re.compile(r'\'{2,5}', re.MULTILINE | re.DOTALL)
pattern_insidelink = re.compile(r'\[\[(?:[^|]*?\|)*?([^|]*?)\]\]', re.MULTILINE | re.DOTALL)
pattern_markup = re.compile(r'\<\/?(ref|br)[^>]*?\>', re.MULTILINE | re.DOTALL)
pattern_outsidelink = re.compile(r'\[(.+\|)*(.+?)\]', re.MULTILINE | re.DOTALL)
pattern_lang = re.compile(r'\{\{lang\|.+?\|(.+?)\}\}', re.MULTILINE | re.DOTALL)

basic_info = {}
with open(sys.argv[1],'r',encoding='utf-8') as britain_file:
    text = britain_file.read()
    for m in pattern.finditer(text):
        removed = pattern_emphasis.sub('',m.group(2))
        removed = pattern_insidelink.sub(r'\1', removed)
        removed = pattern_markup.sub('', removed)
        removed = pattern_outsidelink.sub(r'\2', removed)
        removed = pattern_lang.sub(r'\1', removed)
        basic_info[m.group(1)] = removed

flag_name = basic_info['国旗画像']

url = "https://en.wikipedia.org/w/api.php?"
params = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "titles":"File:{}".format(flag_name),
    "iiprop":"url",
}
r = requests.get(url,params=params).text

print("{}".format(re.findall(r'"url":"(.*?)"',r)))