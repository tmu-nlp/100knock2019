import xml.etree.ElementTree as ET


class Morph:

    def __init__(self, surface: str, base: str, pos: str, pos1: str):
        # 表層形
        self.surface = surface
        # 基本形
        self.base = base
        # 品詞
        self.pos = pos
        # 品詞再分類１
        self.pos1 = pos1

    def print(self):
        print('表層系：{0}, 基本系：{1}, 品詞：{2}, 品詞再分類１：{3}'
              .format(self.surface, self.base, self.pos, self.pos1))


class Chunk:
    def __init__(self, morphs: list, dst: int, srcs: list):
        # Morphのリスト
        self.morphs = morphs
        # 係り先文節インデックス
        self.dst = dst
        # 係り元文節インデックス番号のリスト
        self.srcs = srcs

        # 文節のテキスト
        self.text = ''.join([m.surface for m in self.morphs])

        self.pp = self.returnpp()

    def print(self):
        print(self.text, self.dst)

    # 名詞を持つかどうか
    def hasnoun(self) -> bool:
        # set False for default
        flag = False
        for m in self.morphs:
            if m.pos == '名詞':
                flag = True
        return flag

    # 動詞を持つかどうか
    def hasverb(self) -> bool:
        # set False for default
        flag = False
        for m in self.morphs:
            if m.pos == '動詞':
                flag = True
        return flag

    def hassahen(self) -> bool:
        # set False for default
        flag = False
        for i in range(len(self.morphs)-1):
            if self.morphs[i].pos1 == 'サ変接続' and self.morphs[i+1].base == 'を':
                flag = True
        return flag

    # 述語（一番左の動詞）の基本形を返す
    def predicate(self) -> str:
        verbs = [morph.base for morph in self.morphs if morph.pos == '動詞']
        if verbs != []:
            return verbs[0]
        else:
            return ''

    # 一番右の助詞を返す
    def returnpp(self):
        josi = [morph.base for morph in self.morphs if morph.pos == '助詞']
        if josi != []:
            return josi[-1]
        else:
            return ''

    # 一番左の名詞を返す
    def returnnoun(self):
        nouns = [morph.base for morph in self.morphs if morph.pos == '名詞']
        if nouns != []:
            return nouns[0]
        else:
            return ''


def importchunklists(path: str) -> list:

    # Chunkオブジェクトのリスト[Chunk1, Chunk2, ....]
    chunks = []
    # Chunks list
    chunkslist = []

    tree = ET.parse(path)
    root = tree.getroot()

    for sentences in root:
        # 各文について、各Chunkの係り先文節番号を格納するリスト [2, 2,... -1]
        dsts = []

        chunks = []

        for chunk in sentences.iter('chunk'):

            # 各Chunkについて、morphオブジェクトを格納するリスト [morph1, morph2, ...]
            morphs = []

            # このChunkの文節番号
            id = int(chunk.attrib['id'])

            # このChunkの係り先文節番号
            dst = int(chunk.attrib['link'])

            # この文中のChunkの係り先文節番号を追加
            dsts.append(dst)

            for tok in chunk.iter('tok'):

                # featureを取り出す
                feature = tok.attrib['feature'].split(',')

                base = feature[6]
                pos = feature[0]
                pos1 = feature[1]
                surface = tok.text

                # Morphオブジェクトを作ってリストに追加
                morphs.append(Morph(surface, base, pos, pos1))

            if morphs != []:
                linkedby = [i for i, dst in enumerate(dsts) if dst == id]
                chunks.append(Chunk(morphs, dst, linkedby))

        chunkslist.append(chunks)

    return chunkslist


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)

    for c in clist[7]:
        c.print()


if __name__ == '__main__':
    main()
