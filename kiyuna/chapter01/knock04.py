'''
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine.
 New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19 番目の単語は先頭の 1 文字，
それ以外の単語は先頭に 2 文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への
連想配列（辞書型もしくはマップ型）を作成せよ．
'''


def knock04(s: str) -> dict:
    import re
    nums = [1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2]
    res = {
        word[:num]: idx
        for idx, (num, word)
        in enumerate(zip(nums, re.findall(r'\w+', s)), start=1)
    }
    return res


def element_hunt(s: str) -> dict:
    import re
    elements = {}
    two_letters = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    for atomic_num, word in enumerate(re.findall(r'\w+', s), start=1):
        elements[word[:2 - (atomic_num in two_letters)]] = atomic_num
    return elements


if __name__ == '__main__':
    tgt = "Hi He Lied Because Boron Could Not Oxidize Fluorine."\
          "New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    ans = knock04(tgt)

    assert ans == element_hunt(tgt)

    print(ans)
