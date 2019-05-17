'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
'''
import re

# |フィールド名 = 値
pattern_template = re.compile(r'''
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

# [[記事名]]	
# [[記事名|表示文字]]	
# [[記事名#節名|表示文字]]                        
pattern_internal_link = re.compile(r'''
                        \[\[
                        (?:
                            [^|]*?
                            \|
                        )*
                        ([^|]*?)
                        \]\]''', re.MULTILINE | re.VERBOSE)

# {{lang|言語タグ|文字列}}
pattern_template_lang = re.compile(r'''
                        \{\{
                        (?:[^|]+)
                        \|
                        (?:[^|]+) 
                        \| 
                        ([^|]+) 
                        \}\}''', re.MULTILINE | re.VERBOSE)

# [http://www.example.org 表示文字]
pattern_external_link = re.compile(r'''           
                        \[
                        (?:.+?)
                        \s
                        (.+?)
                        \]
                        ''', re.MULTILINE | re.VERBOSE)

# <br> <br/> <ref> </ref> <ref " ">
pattern_br_ref = re.compile(r''' 
                        <
                        \/?
                        [br|ref]
                        [^>]*?
                        >
                        ''', re.MULTILINE | re.VERBOSE)

info_dict = {}
with open('Briten.txt', encoding='utf-8') as f:
    for match in pattern_template.finditer(f.read()):
        # 強調マークアップを除去
        removed = re.sub(r'\'{2,5}', '', match.group(2)) 
        # MediaWikiマークアップの除去
        removed = pattern_internal_link.sub(r'\1', removed)
        # Template:Langの除去
        removed = pattern_template_lang.sub(r'\1', removed)
        # 外部リンクの除去
        removed = pattern_external_link.sub(r'\1', removed)
        # <ref> <br>の除去
        removed = pattern_br_ref.sub('', removed)

        info_dict[match.group(1)] = removed

for key, value in info_dict.items():
    print(key, value)