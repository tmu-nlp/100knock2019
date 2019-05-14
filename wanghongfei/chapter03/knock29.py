import json, re , requests

def del_highlight(str):
    str = re.sub(r"'{2}(.*)'{2}",r'\1',str)
    return str

def del_link(str):
    str = re.sub(r"\[\[(.*?)\]\]", r'\1', str)
    return str

def del_tri(str):
    str = re.sub(r"<.*>(.*)<.*>", r'\1', str)
    return str

def del_stamp(str):
    str = re.sub(r"\{\{(.*?)\}\}", r'\1', str)
    return str

if __name__ == '__main__':
    jawiki_country = open("./jawiki-country.json", "r")
    for line in jawiki_country:
        json_line = json.loads(line)
        if "イギリス" in json_line["title"]:
         uk = json_line["text"]
    template_regex = re.compile(r'\|(.*?) =(.*?)\n')
    template_info = template_regex.findall(uk)
    
    info_dict = {}
    for item in template_info:
        info_dict[item[0]] = del_tri(del_link(del_highlight(del_stamp(item[1]))))
    
    flag = info_dict['国旗画像']
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action":"query",
        "format":"json",
        "prop": "imageinfo",
        "titles":"File:{}".format(flag),
        }
    R = requests.get(url=URL, params=PARAMS).text
    print(R)
