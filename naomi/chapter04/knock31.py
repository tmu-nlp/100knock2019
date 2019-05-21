from knock30 import importmecab

# 31. 動詞
# 動詞の表層形をすべて抽出せよ．


def surfaceverb(sentences: list) -> list:
    surfaces = []
    for morphs in sentences:
        for m in morphs:
            if m['pos'] == u'動詞':
                surfaces.append(m['surface'])
    return surfaces


def main():
    path = 'neko.txt.mecab'
    surfaces = surfaceverb(importmecab(path))
    with open('knock31.txt', 'w', encoding='utf-8') as f:
        print(surfaces, file=f)


if __name__ == '__main__':
    main()
