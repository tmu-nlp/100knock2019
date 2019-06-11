import pymongo
from flask import Flask, request

app = Flask(__name__)


def render_template_(result):
    template = f'''
<html>
    <head>
        <meta charset="utf-8">
        <title>knock69</title>
    </head>
    <body>
    <p>[<a href="/">RELOAD</a>]</p>
    <form action="/" method="POST">
        <p>名前/別名: <input type="text" name="name"></p>
        <p>タグ : <input type="text" name="tag"></p>
        <p><input type="submit" value="検索"></p>
    </form>
    <hr>
    <div>
        {result}
    </div>
    </body>
</html>
'''
    return template


def search(name, tag):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.knock64_DB
    collection = db.collection_artists

    if name != '' and tag != '':
        return list(collection.find({'$and': [{'$or': [{'name': name}, {'aliases.name': name}]}, {'tags.value': tag}]}).sort("rating.count", pymongo.DESCENDING))
    elif name != '':
        return list(collection.find({'$or': [{'name': name}, {'aliases.name': name}]}).sort("rating.count", pymongo.DESCENDING))
    elif tag != '':
        return list(collection.find({'tags.value': tag}).sort("rating.count", pymongo.DESCENDING))
    else:
        return ''


def format(data_list):
    result = []
    for data in data_list:
        if 'name' in data:
            name = data['name']
        if 'area' in data:
            area = data['area']
        tags = []
        if 'tags' in data:
            for tag_dics in data['tags']:
                tags.append(tag_dics['value'])
        aliases = []
        if 'aliases' in data:
            for aliase_dics in data['aliases']:
                aliases.append(aliase_dics['name'])

        result.append(
            f'name : {name}<br/>\narea : {area}<br/>\ntags : {", ".join(tags)}<br/>\naliases : {", ".join(aliases)}')

    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        result = format(search(request.form['name'], request.form['tag']))
    return render_template_('<br/></br>\n'.join(result))


if __name__ == '__main__':
    app.run(debug=True)
