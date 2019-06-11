'''
69. Webアプリケーションの作成
ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．
アーティスト名，アーティストの別名，タグ等で検索条件を指定し，
アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．
'''
import sys
from bottle import run, get, request
from itertools import islice


def message(text):
    sys.stderr.write(f"\33[92m{text}\33[0m\n")


@get('/search')
def render():
    name = request.query.name
    aliases_name = request.query.aliases_name
    name_alias = request.query.getunicode('name_alias')
    tag = request.query.get('tag')

    query = {}
    if name:
        query['name'] = name
    else:
        name = ""
    if aliases_name:
        query['aliases.name'] = aliases_name
    else:
        aliases_name = ""
    if name_alias:
        query['$or'] = [{'name': name_alias}, {'aliases.name': name_alias}]
    else:
        name_alias = ""
    if tag:
        query['tags.value'] = tag
    else:
        tag = ""

    message(str(query))
    res = []
    for d in islice(collection.find(query), 50):
        alname = d['aliases'][0]['name'] if 'aliases' in d else 'データなし'
        tags = ', '.join(
            tag['value'] for tag in d['tags']) if 'tags' in d else 'データなし'
        rate = d['rate']['value'] if 'rate' in d else 'データなし'
        res.append(
            f"[名前] {d['name']}<br>"
            f"[別名] {alname}<br>"
            f"[タグ] {tags}<br>"
            f"[レート] {rate}"
        )
    size = len([*islice(collection.find(query), 10001)])
    if size >= 10001:
        size = '10000 以上'
    result = f"{len(res)} / {size} 件表示<br><hr>"
    result += '<br><br>'.join(res)

    return f'''
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <form action="/search" method="get">
        名前: <input name="name" type="text" value="{name}"/>
        別名: <input name="aliases_name" type="text" value="{aliases_name}"/>
        名前/別名: <input name="name_alias" type="text" value="{name_alias}"/><br>
        タグ: <input name="tag" type="text" value="{tag}"/><br>
        <input value="検索" type="submit" />
    </form>
    <hr>
    <div>{result}</div>
    '''


if __name__ == '__main__':
    from pymongo import MongoClient, DESCENDING
    collection = MongoClient('localhost', 27017).artist_db.artist_collection
    run(host='localhost', port=8080, debug=True)


'''
* Bottle
    - https://qiita.com/masaibar/items/e3b6911aee6741037549
* OR 検索
    - https://docs.mongodb.com/manual/reference/operator/query/or/
    - https://docs.mongodb.com/manual/reference/operator/query/and/
'''
