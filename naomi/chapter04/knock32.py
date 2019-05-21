from knock30 import importmecab

# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．


def baseverb(sentences: list) -> list:
    surfaces = []
    for morphs in sentences:
        for m in morphs:
            if m['pos'] == u'動詞':
                surfaces.append(m['base'])
    return surfaces


def main():
    path = 'neko.txt.mecab'
    surfaces = baseverb(importmecab(path))
    with open('knock32.txt', 'w', encoding='utf-8') as f:
        print(surfaces, file=f)


if __name__ == '__main__':
    main()
