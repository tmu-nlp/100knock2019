from knock30 import importmecab


def baseverb(sentences: list) -> list:
    surfaces = []
    for morphs in sentences:
        for m in morphs:
            if m['pos'] == u'名詞':
                if m['pos1'] == u'サ変接続':
                    surfaces.append(m['base'])
    return surfaces


def main():
    path = 'neko.txt.mecab'
    surfaces = baseverb(importmecab(path))
    with open('knock33.txt', 'w', encoding='utf-8') as f:
        print(surfaces, file=f)


if __name__ == '__main__':
    main()