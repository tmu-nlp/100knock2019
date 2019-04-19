'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば "I couldn't believe that I could actually understand
what I was reading : the phenomenal power of the human mind ."）を与え，
その実行結果を確認せよ．
'''


def typoglycemia(src: str) -> str:
    import random

    res = []
    for word in src.split(' '):
        if len(word) > 4:
            head, *middle, tail = word
            random.shuffle(middle)
            word = head + ''.join(middle) + tail
        res.append(word)

    return ' '.join(res)


if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand "\
               "what I was reading : the phenomenal power of the human mind ."

    print(typoglycemia(sentence))
