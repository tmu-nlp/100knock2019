from knock30 import importmecab

# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．


def ext_np(sentences: list) -> list:
    surfaces = []
    for morphs in sentences:
        for i in range(2, len(morphs)):
            if morphs[i-2]['pos'] == u'名詞':
                if morphs[i-1]['surface'] == u'の':
                    if morphs[i]['pos'] == u'名詞':
                        surfaces.append(morphs[i-2]['surface']
                                        + morphs[i-1]['surface']
                                        + morphs[i]['surface'])
    return surfaces


def main():
    path = 'neko.txt.mecab'
    surfaces = ext_np(importmecab(path))
    with open('knock34.txt', 'w', encoding='utf-8') as f:
        print(surfaces, file=f)


if __name__ == '__main__':
    main()
