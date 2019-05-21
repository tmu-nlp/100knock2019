'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．
'''
# Python 3.6.2 で実行
import re
import pprint
from collections import OrderedDict, defaultdict
from knock25 import extract_infobox


def remove_em(d: OrderedDict) -> OrderedDict:
    """ remove emphasis syntax
    """
    reg = re.compile(r"'{2,}")
    for key, value in d.items():
        d[key] = reg.sub('', value)
    return d


def remove_double_square_brackets(d: OrderedDict) -> OrderedDict:
    """ replace interwiki link and extended image syntax
        for displayed characters
    """
    reg = re.compile(r'\[\[.*?([^\|]+?)\]\]')
    for key, value in d.items():
        d[key] = reg.sub(r'\1', value)
    return d


def remove_single_square_bracket(d: OrderedDict) -> OrderedDict:
    """ replace external link for displayed characters
    """
    reg = re.compile(r'\[.*?([^ \|]+?)\]')
    for key, value in d.items():
        d[key] = reg.sub(r'\1', value)
    return d


def remove_double_curly_brackets(d: OrderedDict) -> OrderedDict:
    """ reshape lang templates
    """
    reg = re.compile(r'{{lang\|(?P<Lang_tag>.+?)\|(?P<Text>.+?)}}')
    for key, value in d.items():
        d[key] = reg.sub(r'\g<Text> [\g<Lang_tag>]', value)
    return d


def remove_ref(d: OrderedDict) -> OrderedDict:
    """ remove footnotes
    """
    reg = re.compile(r'(<ref( name=".+?")?>.*?</ref>|<ref name=".+?" />)')
    for key, value in d.items():
        d[key] = reg.sub('', value)
    return d


def remove_br(d: OrderedDict) -> OrderedDict:
    """ remove <br />
    """
    reg = re.compile(r'<br\s?/>')
    for key, value in d.items():
        d[key] = reg.sub('', value)
    return d


def remove_markup(d: OrderedDict) -> OrderedDict:
    """ remove_markup
        = remove_em
        + remove_double_square_brackets
        + remove_double_curly_brackets
        + remove_ref
        + remove_br
    """
    ptn_repl = {
        # remove emphasis syntax
        r"'{2,}": '',
        # replace interwiki link and extended image syntax for displayed characters
        r'\[\[.*?([^\|]+?)\]\]': r'\1',
        # reshape lang templates
        r'{{lang\|(?P<Lang_tag>.+?)\|(?P<Text>.+?)}}': r'\g<Text> [\g<Lang_tag>]',
        # remove footnotes
        r'(<ref( name=".+?")?>.*?</ref>|<ref name=".+?" />)': '',
        # remove <br />
        r'<br\s?/>': '',
    }
    for ptn, repl in ptn_repl.items():
        reg = re.compile(ptn)
        for key, value in d.items():
            d[key] = reg.sub(repl, value)
    return d


def remove_asterisks_in_ref(d: OrderedDict) -> OrderedDict:
    """ reshape bulleted list
    """
    import sys
    reg = re.compile(r'(.+?)<ref>([^:]+):(.+?)</ref>', re.DOTALL)
    res_keys = list(d.keys())
    res = dict(d)
    for key, value in d.items():
        m = reg.search(value)
        if m:
            res[key], sub = m.group(1, 2)
            cnt = defaultdict(int)
            new_keys = []
            prev_lv = 0
            for e in m.group(3).strip().split('\n'):
                ast, txt = re.match('(\**)([^\*]+)', e).group(1, 2)
                lv = len(ast)
                if prev_lv > lv:
                    cnt[lv + 1] = 0
                cnt[lv] += 1
                new_k = f'{sub}'
                for i in range(1, lv + 1):
                    new_k += f'-{cnt[i]:02d}'
                new_keys.append(new_k)
                res[new_k] = txt
                prev_lv = lv
            for i, k in enumerate(new_keys, start=1):
                res_keys.insert(res_keys.index(key) + i, k)
    return OrderedDict((k, res[k]) for k in res_keys)


if __name__ == '__main__':
    d = extract_infobox()
    d = remove_em(d)
    d = remove_double_square_brackets(d)
    d = remove_single_square_bracket(d)      # remove_ref を実行するので不要
    d = remove_double_curly_brackets(d)
    d = remove_ref(d)
    d = remove_br(d)
    d = remove_asterisks_in_ref(d)
    pprint.pprint(d)

    assert d == remove_asterisks_in_ref(remove_markup(extract_infobox()))


''' NOTE
* マークアップ早見表
-> https://ja.wikipedia.org/wiki/Help:早見表

* ウィキペディアの <ref>
-> https://en.wikipedia.org/wiki/Wikipedia:Citing_sources

* ウィキペディアの基礎情報に置ける公式国名の表記
-> https://ja.wikipedia.org/wiki/Template:基礎情報_国#公式国名

* ウィキペディアの言語タグ
-> https://ja.wikipedia.org/wiki/Template:Lang
    {{lang|言語タグ|文字列}}
'''
