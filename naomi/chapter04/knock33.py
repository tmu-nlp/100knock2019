from knock30 import importmecab

# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．


def ext_sahen(sentences: list) -> list:
    surfaces = []
    for morphs in sentences:
        for m in morphs:
            if m['pos'] == u'名詞':
                if m['pos1'] == u'サ変接続':
                    surfaces.append(m['base'])
    return surfaces


def main():
    path = 'neko.txt.mecab'
    surfaces = ext_sahen(importmecab(path))
    with open('knock33.txt', 'w', encoding='utf-8') as f:
        print(surfaces, file=f)


if __name__ == '__main__':
    main()
