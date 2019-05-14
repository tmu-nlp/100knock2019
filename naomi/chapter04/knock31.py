from knock30 import importmecab


def surfaceverb(sentences: list) -> list:
    surfaces = []
    for morphs in sentences:
        for m in morphs:
            if m['pos'] == u'動詞':
                surfaces.append(m['surface'])
    return surfaces


def main():
    path = 'neko.txt.mecab'
    print(importmecab(path))
    surfaces = surfaceverb(importmecab(path))


if __name__ == '__main__':
    main()