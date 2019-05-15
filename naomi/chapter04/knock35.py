from knock30 import importmecab


def baseverb(sentences: list) -> list:
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
    surfaces = baseverb(importmecab(path))
    with open('knock35.txt', 'w', encoding='utf-8') as f:
        print(surfaces, file=f)


if __name__ == '__main__':
    main()