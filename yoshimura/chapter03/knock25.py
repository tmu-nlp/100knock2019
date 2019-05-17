'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
'''
import re

# # {{基礎情報 国 ~ }}
# pattern_base_info = re.compile(r'''
#                                 ^\{\{基礎情報\s.+?$
#                                 (?P<base_info>.+?)
#                                 ^\}\}$
#                                 ''',re.MULTILINE | re.DOTALL | re.VERBOSE)

# |フィールド名 = 値
pattern = re.compile(r'''
                        ^
                        \|
                        (?P<field>.+?)
                        \s
                        =
                        \s
                        (?P<value>.+?)
                        (?=
                            \n
                            (\||\})
                        )
                     ''', re.MULTILINE | re.DOTALL | re.VERBOSE)

info_dict = {}
with open('Briten.txt', encoding='utf-8') as f:
    text = f.read()
    for match in pattern.finditer(text):
        info_dict[match.group('field')] = match.group('value')

for key, value in info_dict.items():
    print(f"{key}:\t{value}")

# X(?=Y) Xの後ろにYがあるXにマッチ
# MULTILINE 複数行マッチ
# DOTALL . が改行を含むすべての文字をマッチするようになる
# VERBOSE 空白が無視される