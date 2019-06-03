import xml.etree.ElementTree as ET
from collections import defaultdict

replace_dic = {}
tree = ET.parse('nlp.txt.xml')


for coreference in tree.iterfind('.//coreference/coreference'):
    for mention in coreference.iterfind('./mention'):
        if 'representative' in mention.attrib and mention.attrib['representative']:
            repre_mention = mention.findtext('text')
        else:
            sentence_id = int(mention.findtext('sentence'))
            start_id = int(mention.findtext('start'))
            end_id = int(mention.findtext('end'))
            replace_dic[sentence_id, start_id] = (end_id, repre_mention)

for sentence in tree.iterfind('.//sentences/sentence'):
    end_id_dic = defaultdict(lambda: 0)
    sentence_id = int(sentence.get('id'))
    for token in sentence.iterfind('./tokens/token'):
        token_id = int(token.get('id'))
        if (sentence_id, token_id) in replace_dic:
            end_id, representative = replace_dic[sentence_id, token_id]
            end_id_dic[end_id-1] += 1
            print(f'「{representative} (', end='')
        print(token.findtext('word'), end='')
        while end_id_dic[token_id] != 0:
            print(') 」', end='')
            end_id_dic[token_id] -= 1
        print(' ', end='')
    print('')
