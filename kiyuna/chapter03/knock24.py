'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''
import re


def extract_file_names():
    ptn1 = r'([^<{]+\.)(?i)(png|gif|jpg|jpeg|xcf|pdf|mid|ogg|svg|djvu)'
    reg1 = re.compile(ptn1)
    ptn2 = r'(.+)\s*[=|:]+?\s*(?P<File_name>.+)'
    reg2 = re.compile(ptn2)
    res = []
    with open('wiki_UK.txt') as f:
        for line in f:
            print(reg1.findall(line))
            for name, ext in reg1.findall(line):
                if '/' not in name:
                    res.append(reg2.match(name).group('File_name') + ext)
    return res


if __name__ == '__main__':
    # [*] tgt = r'\[\[(?P<namespace>[^:\]]+):(?P<File_name>[^|]+).*?\]\]'
    # => ファイル・File 以外にマッチしたのは Category だけ
    # [x] tgt = r'\[\[(ファイル|File):(?P<File_name>[^|]+).*\]\]'
    # => <gallery> タグ内の画像が拾えない
    #    「ファイル:PalaceOfWestminsterAtNight.jpg|[[ウェストミンスター宮殿]]」
    # [*] tgt = r'(?:File|ファイル):([^\|]+)'
    # => 他にもファイルがないか探す
    # [*] tgt = r'{{[^}]*}}'
    # => メディアファイルは見つからなかった
    # [*] tgt = r'.*\.(?:png|gif|jpg|jpeg|xcf|pdf|mid|ogg|svg|djvu)'
    # =>「{{基礎情報 国
    #     |略名 = イギリス」の部分に国旗等の画像ファイルを見つけた
    # => 「{{PDFlink|[http://www.mod.uk/（略）/modara_0405_s1_resources.pdf」
    #    「<ref>[http://www.atkearney.com/（略）Present+and+Future-GCI+2014.pdf」
    #     といったファイルも引っかかってしまう
    fnames = extract_file_names()
    print(f"\033[32m[+] found {len(fnames)} files\033[00m")
    print(*fnames, sep='\n')


''' NOTE
* ウィキペディアの画像
-> https://ja.wikipedia.org/wiki/Help:画像の表示#要点
    書式：[[ファイル:ファイル名|オプション]]
    プレフィックスは File でも機能します（[[File:ファイル名|オプション]]）。

* ウィキペディアの名前空間
-> https://ja.wikipedia.org/wiki/Help:名前空間

* ウィキペディアの <gallery>
-> https://en.wikipedia.org/wiki/Help:Gallery_tag

* ウィキペディアでは画像などのファイルをアップロードし、
  そのファイルをページ中に挿入することができる
-> https://ja.wikipedia.org/wiki/Help:画像などのファイルのアップロードと利用
    ウィキメディア・プロジェクトで許可されているファイル形式は、
    拡張子が png, gif, jpg, jpeg, xcf, pdf, mid, ogg, svg, djvu のいずれか
    となるものです。

* 特殊文字
-> https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
    * `(?:...)`:
        普通の丸括弧の、キャプチャしない版です。
    * `(?<!...)`:
        その文字列における現在位置の前に ... とのマッチがなければ、マッチします。
        これは 否定後読みアサーション(negative lookbehind assertion) と呼ばれます。

* モジュールコンテンツ
-> https://docs.python.org/ja/3/library/re.html?highlight=findall#module-contents
    * re.IGNORECASE / re.I
        大文字・小文字を区別しないマッチングを行います;
        [A-Z] のような正規表現は小文字にもマッチします。
        インラインフラグの (?i) に相当します。
'''
