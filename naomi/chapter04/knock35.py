from knock30 import importmecab

# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


def ext_rensetu(sentences: list) -> list:
    rensetu = []
    for morphs in sentences:
        # 新しい文をみるときにmeisiをリセット
        meisi = ''
        for m in morphs:
            if m['pos'] == u'名詞':
                # 名詞であればとにかくつなげる
                meisi += m['surface']
            else:
                if meisi != '':
                    # rensetu listにmeisiを格納
                    rensetu.append(meisi)
                    # meisiを一度リセット
                meisi = ''
    return rensetu


def main():
    path = 'neko.txt.mecab'
    surfaces = ext_rensetu(importmecab(path))
    with open('knock35.txt', 'w', encoding='utf-8') as f:
        print(surfaces, file=f)


if __name__ == '__main__':
    main()
