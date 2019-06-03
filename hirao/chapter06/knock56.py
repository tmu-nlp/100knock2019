import termcolor
import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")
mention_dict = {}

# 参照
for coreference in root.iterfind("./document/coreference/coreference"):
    text = coreference.findtext("./mention[@representative='true']/text")
    # 参照を全て格納しておく
    for mention in coreference.iterfind('./mention'):
        if mention.get('representative', 'false') == 'false':
            sentence_id, start, end = int(mention.findtext('sentence')), int(
                mention.findtext('start')), int(mention.findtext('end'))
            # 参照リストに入っていなければ追加
            if not (sentence_id, start) in mention_dict:
                mention_dict[(sentence_id, start)] = (end, text)

# 本文の表示
# 参照がある部分は参照を追加
for sentence in root.iterfind("./document/sentences/sentence"):
    sentence_id = int(sentence.get('id'))
    original_rest = 0

    for token in sentence.iterfind("./tokens/token"):
        token_id = int(token.get('id'))
        # 参照表現の途中でなく、参照一覧に現在の文idとトークンidがある場合
        if original_rest == 0 and (sentence_id, token_id) in mention_dict:

            (end, mention_text) = mention_dict[(sentence_id, token_id)]
            # 着色
            mention_text = termcolor.colored(mention_text, 'blue')
            # [代表参照表現](参照表現)
            print('[' + mention_text + '] (', end='')
            original_rest = end - token_id

        print(token.findtext('word'), end='')

        # 参照の最中である場合
        # 最後に)をつける
        if original_rest > 0:
            original_rest -= 1
            if original_rest == 0:
                print(')', end='')
        print(' ', end='')
    print("\n")
