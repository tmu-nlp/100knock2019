import plyvel
import json
import pickle


def make_db():
    try:
        # 存在しない場合作成，存在する場合エラー
        db = plyvel.DB('./db_knock63/', create_if_missing=True, error_if_exists=True)
        for line in open('artist.json', 'r'):
            artist_dic = json.loads(line)
            if {'name', 'tags'}.issubset(set(artist_dic.keys())):
                db.put(artist_dic['name'].encode('utf-8'), json.dumps(artist_dic['tags']).encode('utf-8'))
        db.close()
    except:
        pass


def search_tags(name):
    db = plyvel.DB('./db_knock63/')
    try:
        tags = json.loads(db.get(name.encode('utf-8')))
    except TypeError:
        tags = 'The artist name is not registered.'
    db.close()
    return tags


if __name__ == '__main__':
    make_db()
    while True:
        input_text = input('Please enter an artist name. (quit command: "q")\nartist name: ')
        if input_text == 'q':
            break
        else:
            tags = search_tags(input_text)
            print(f'tags : {tags}')
            print('-'*100)
