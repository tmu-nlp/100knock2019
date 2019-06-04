import xml.etree.ElementTree as ET


class Morph:

    def __init__(self, surface: str, base: str, pos: str, pos1: str):
        # 表層形
        self.s = surface
        # 基本形
        self.b = base
        # 品詞
        self.p = pos
        # 品詞再分類１
        self.p1 = pos1

    def print(self):
        print('表層系：{0}, 基本系：{1}, 品詞：{2}, 品詞再分類１：{3}'
              .format(self.s, self.b, self.p, self.p1))


class Chunk:
    def __init__(self, ms: list, d: int, s: list):
        # Morphのリスト
        self.morphs = []
        # 係り先文節インデックス
        self.dst = 0
        # 係り元文節インデックス番号のリスト
        self.srcs = []


def importmorphlists(path: str) -> list:

    # morphオブジェクトリストのリスト[[morph1, morph2, ...], [morph 9, morph 10, ....]
    mlists = []
    tree = ET.parse(path)
    root = tree.getroot()

    for sentences in root:
        # 各文について、morphオブジェクトを格納するリスト [morph1, morph2, ...]
        morphs = []

        for tok in sentences.iter('tok'):

            # featureを取り出す
            feature = tok.attrib['feature'].split(',')

            base = feature[6]
            pos = feature[0]
            pos1 = feature[1]
            surface = tok.text

            # Morphオブジェクトを作ってリストに追加
            morphs.append(Morph(surface, base, pos, pos1))

        if morphs != []:
            mlists.append(morphs)

    return mlists


def main():
    path = 'neko.txt.cabocha'
    mlists = importmorphlists(path)

    for m in mlists[2]:
        m.print()


if __name__ == '__main__':
    main()
