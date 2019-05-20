'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
（参考: マークアップ早見表）．
'''
import re

# |フィールド名 = 値
pattern = re.compile(r'''
                        ^
                        \|
                        (.+?)
                        \s
                        =
                        \s
                        (.+?)
                        (?=
                            \n
                            (\||\})
                        )
                     ''', re.MULTILINE | re.DOTALL | re.VERBOSE)

info_dict = {}
with open('Briten.txt', encoding='utf-8') as f:
    for match in pattern.finditer(f.read()):
        # 強調マークアップ除去
        info_dict[match.group(1)] = re.sub(r'\'{2,5}', '', match.group(2)) 

for key, value in info_dict.items():
    print(f"{key}:\t{value}")