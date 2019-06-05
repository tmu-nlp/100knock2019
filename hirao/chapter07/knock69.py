from flask import Flask, request, redirect, url_for
from pymongo import MongoClient, DESCENDING
from typing import Optional

app = Flask(__name__)

# HTML テンプレートの文字列を返す
def render_template(result: str) -> str:
    template = f"""
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
"""
    return template


# name and/or tag で MongoDB を検索する
def search(name: str, tag: str) -> list:
    client = MongoClient()
    database = client.testdb
    collection = database.artist

    query = {}  # type: dict
    if name != "" and tag != "":
        query = {
            "$and": [
                {"$or": [{"name": name}, {"aliases.name": name}]},
                {"tags_value": tag},
            ]
        }
    elif name != "":
        query = {"$or": [{"name": name}, {"aliases.name": name}]}
    elif tag != "":
        query = {"tags.value": tag}

    response = list(collection.find(query).sort("rating.count", DESCENDING))
    return response


def doc2string(doc: dict, key: str, spec: Optional[str]) -> str:
    result = ""
    if key in doc:
        if type(doc[key]) == list:
            if spec:
                doc[key] = [f"{val[spec]}" for val in doc[key]]
            result = " , ".join([f"{val}" for val in doc[key]])
        elif type(doc[key]) == dict:
            result = f"{doc[key][spec]}"
        else:
            result = f"{doc[key]}"
    else:
        result = "(データなし)"
    return result


# DB 検索結果をページに表示するために整形する
def format_result(res: list) -> str:
    if res == []:
        return "一致する情報は見つかりませんでした"
    info = ["[名前]", "[別名]", "[場所]", "[タグ]", "[レーティング]"]
    keys = ["name", "aliases", "area", "tags", "rating"]
    specs = [None, "name", None, "value", "count"]

    formatted_result = ""
    for num, r in enumerate(res):
        results = []
        for key, spec in zip(keys, specs):
            results.append(doc2string(r, key, spec))
        formatted_result += f"<div class='content_{num}'><p>"
        for i, result in zip(info, results):
            formatted_result += f"{i} : {result}<br/>\n"
        formatted_result += "</p></div>"
    return formatted_result


# GET/POST に応じてページを返す
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        search_result = search(request.form["name"], request.form["tag"])
        result = format_result(search_result)
    return render_template(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)