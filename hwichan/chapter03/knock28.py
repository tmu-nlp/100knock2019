import gzip
import json
import re


def read_json(filename: str, title: str) -> str:
    with gzip.open(filename, "rt", "utf_8") as f:
        for line in f:
            json_data = json.loads(line)  # jsonデータを辞書型に変換
            if json_data['title'] == title:
                return json_data['text']


def make_dict(text: str) -> dict:
    # 基礎情報の抽出
    pattern = re.compile(r'''
                            ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
                            (.*?)       # キャプチャ対象
                            ^\}\}$      # '}}'の行
                            ''', re.MULTILINE + re.VERBOSE + re.DOTALL)  # .を改行(\n)にもマッチさせるre.DOTALL

    contents = pattern.findall(text)

    # フィールド名の抽出 フィールド名は行頭が |
    pattern = re.compile(r'''
                            ^\|         # '|'で始まる行
                            (.+?)       # キャプチャ対象（フィールド名）
                            \s*         # 空白文字0文字以上
                            =
                            \s*         # 空白文字0文字以上
                            (.+?)       # キャプチャ対象（値）
                            (?:         # キャプチャ対象外のグループ開始
                                (?=\n\|)    # 改行+'|'の手前、基本的にはこっち
                                | (?=\n$)   # 改行+終端の手前、最終行のみ
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
                                [^\s]*? # 空白以外の文字が0文字以上
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
                            )*? # グループが0以上出現
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
    text = read_json("jawiki-country.json.gz", "イギリス")
    temp_dict = make_dict(text)

    for key, value in temp_dict.items():
        temp_dict[key] = markup_delete(value)

    for j in temp_dict:
        print('{0} : {1}'.format(j, temp_dict[j]))


if __name__ == '__main__':
    main()
