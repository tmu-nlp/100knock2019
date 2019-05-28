'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
'''
import sys
import gzip
import json
import pprint


def extract_wiki(title):
    with gzip.open('jawiki-country.json.gz', 'rt') as f:    # テキストモード
        for line in f:
            d = json.loads(line)
            if d['title'] == title:
                return d['text']


def main():
    article = extract_wiki(title='イギリス')
    with open('wiki_UK.txt', 'w') as f:
        f.write(article)
    print('[+] wiki_UK.txt', file=sys.stderr)


if __name__ == '__main__':
    main()

    # 以下，json と遊ぶ
    with gzip.open('jawiki-country.json.gz', mode='rt') as f:
        article = json.loads(f.readline())
        sys.stderr.writelines(''.join(map(lambda x: f"\033[33m{x}\033[00m\n", [
            type(article),      # => <class 'dict'>
            article.keys()      # => dict_keys(['text', 'title'])
        ])))
        #pprint.pprint(article, stream=sys.stderr)


''' NOTE
* gzip.open 関数
-> https://docs.python.org/ja/3/library/gzip.html#gzip.open
    引数 mode には、
    バイナリモード用に 'r'、'rb'、'a'、'ab'、'w'、'wb'、'x'、または 'xb'、
    テキストモード用に 'rt'、'at'、'wt'、または 'xt' を指定できます。
    デフォルトは 'rb' です。

cf. open 関数
-> https://docs.python.org/ja/3/library/functions.html?highlight=open#open
    mode はオプションの文字列で、ファイルが開かれるモードを指定します。
    デフォルトは 'r' で、読み込み用にテキストモードで開くという意味です。
    その他のよく使われる値は、書き込み
    (ファイルがすでに存在する場合はそのファイルを切り詰めます) 用の 'w'、
    排他的な生成用の 'x'、追記用の 'a' です
    (いくつかの Unix システムでは、全て の書き込みが現在のファイルシーク位置に
    関係なくファイルの末尾に追加されます)。
    テキストモードでは、encoding が指定されていない場合に使われるエンコーディングは
    プラットフォームに依存します:locale.getpreferredencoding(False) を使って
    現在のロケールエンコーディングを取得します。
    (rawバイト列の読み書きには、バイナリモードを使い、encoding は未指定のままとします)
    指定可能なモードは次の表の通りです。
        文字	意味
        'r'	読み込み用に開く (デフォルト)
        'w'	書き込み用に開き、まずファイルを切り詰める
        'x'	排他的な生成に開き、ファイルが存在する場合は失敗する
        'a'	書き込み用に開き、ファイルが存在する場合は末尾に追記する
        'b'	バイナリモード
        't'	テキストモード (デフォルト)
        '+'	ディスクファイルを更新用に開く (読み込み／書き込み)
    デフォルトのモードは 'r' (開いてテキストの読み込み、'rt' と同義) です。
    バイナリの読み書きアクセスについては、
    モード 'w+b' はファイルを開いて 0 バイトに切り詰めます。
    'r+b' はファイルを切り詰めずに開きます。

* イギリス（wiki）
-> https://ja.wikipedia.org/wiki/イギリス

* MEMO
from io import StringIO
with gzip.open(fname, "rt") as f:
    for line in f:
        json_data = json.load(StringIO(line))
'''
