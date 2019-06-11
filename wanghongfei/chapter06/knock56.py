import xml.etree.ElementTree as ET

xml_tree = ET.parse("/users/hongfeiwang/nlp.txt.xml")
#XMLから文を読み込み、リストで保存
sentences = []
for sentence in xml_tree.iter("sentence"):
    words = []
    for word in sentence.iter("word"):
        words.append(word.text)
    if words:
        sentences.append(words)
#参照関係を読み込み
mentions = []
for mention in xml_tree.iter("mention"):
    if mention.get("representative") == 'true':
        repre = mention.find("text").text
    else:
        mentions.append([
                        int(mention.find("sentence").text) - 1,
                        int(mention.find("start").text) - 1,
                        int(mention.find("end").text) - 1,
                        repre
                        ])
#文の置換
for mention in mentions:
    sentences[mention[0]].insert(mention[2],"(" + mention[3] + ")" )
for sentence in sentences:
    print(" ".join(sentence))
