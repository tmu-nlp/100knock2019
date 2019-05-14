import requests
import gzip
import json
import re
import urllib.parse, urllib.request


def read_json(filename: str, title: str) -> str:
    with gzip.open(filename, "rt", "utf_8") as f:
        for line in file:
            json_data = json.loads(line)  # jsonデータを辞書型に変換
            if json_data['title'] == title:
                return json_data['text']


def make_dict(text: str) -> dict:
    pattern = re.compile(r'''
                            ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
                            (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
                            ^\}\}$      # '}}'の行
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)  # .を改行(\n)にもマッチさせるre.DOTALL

    contents = pattern.findall(text)

    pattern = re.compile(r'''
                            ^\|         # '|'で始まる行
                            (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
                            \s*         # 空白文字0文字以上
                            =
                            \s*         # 空白文字0文字以上
                            (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
                            (?:         # キャプチャ対象外のグループ開始
                                (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
                                | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
                            )           # グループ終了
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

    pattern_list = pattern.findall(contents[0])

    temp_dict = {}
    for i in pattern_list:
        temp_dict[i[0]] = i[1]

    return temp_dict


def markup_delete(text: str) -> str:

    # 強調マークアップ
    pattern = re.compile(r'''
                            \'{2,} #二個以上の'
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

    s = pattern.sub('', text)

    # 内部リンク、ファイル
    pattern = re.compile(r'''
                            \[\[
                            (?:
                                [^|]*?
                                \|
                            )*?
                            ([^|]*?)
                            \]\]
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    s = pattern.sub(r'\1', s)

    # 外部リンク  [http://xxxx] 、[http://xxx xxx]
    pattern = re.compile(r'''
                            \[http:\/\/
                            (?:
                                [^\s]*?
                                \s
                            )?
                            ([^]]*?)
                            \]
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    s = pattern.sub(r'\1', s)

    # Template:Lang  {{lang|言語タグ|文字列}}
    pattern = re.compile(r'''
                            \{\{
                            (?:
                                [^|]*?
                                \|
                            )*?
                            ([^|]*?)
                            \}\}
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    s = pattern.sub(r'\1', s)

    # <br>、<ref>
    pattern = re.compile(r'''
                            <
                            \/?
                            [^>]*?
                            >
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)
    s = pattern.sub('', s)

    return s


def main():
    text = read_json("jawiki-country.json.gz", "オランダ")
    temp_dict = make_dict(text)

    for key, value in temp_dict.items():
        temp_dict[key] = markup_delete(value)

    # urllib.parse.quote 引数の文字列をエンコード
    url = 'https://www.mediawiki.org/w/api.php?' \
        + 'action=query' \
        + '&format=json' \
        + '&prop=imageinfo' \
        + '&titles=File:' + urllib.parse.quote(temp_dict['国旗画像']) \
        + '&iiprop=url'

    connection = urllib.request.urlopen(url)

    # urlのjsonとして受信
    data = json.loads(connection.read().decode())

    # URL取り出し
    url = data['query']['pages']['-1']['imageinfo'][0]['url']
    print(url)


if __name__ == '__main__':
    main()
