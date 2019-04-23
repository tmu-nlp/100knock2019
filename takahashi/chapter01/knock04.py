# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字
# それ以外の単語は先頭に2文字を取り出し
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

from typing import Dict

def make_dict_of_elemental_symbols(target: str) -> Dict[str, str]:
    result = {}
    words = target.split(" ")
    nums = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    # 
    for index, word in enumerate(words, start=1):
        if index in nums:
            result[word[0:1]] = index
        else:
            result[word[0:2]] = index

    return result

if __name__ == "__main__":
    target = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    print(make_dict_of_elemental_symbols(target))
