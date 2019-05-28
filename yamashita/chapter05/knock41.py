import re
from knock40 import Morph


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        surfaces = ''
        for morph in self.morphs:
            surfaces += morph.surface
        return f'{surfaces} {self.dst}'

    def surface(self):
        surfaces = ''
        for morph in self.morphs:
            surfaces += morph.surface
        return surfaces

    def no_sign_surface(self):
        surfaces = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                surfaces += morph.surface
        return surfaces

    def has_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

    def get_allsurfaces_base(self, key, value):
        surfaces = []
        if key == 'pos':
            for morph in self.morphs:
                if morph.pos == value:
                    surfaces.append(morph.base)
            return surfaces
        if key == 'pos1':
            for morph in self.morphs:
                if morph.pos1 == value:
                    surfaces.append(morph.base)
            return surfaces

    def get_sahensetuzoku_wo(self):
        for i in range(len(self.morphs)-1):
            if self.morphs[i].pos == '名詞' and self.morphs[i].pos1 == 'サ変接続' and self.morphs[i+1].surface == 'を' and self.morphs[i+1].pos == '助詞':
                return self.morphs[i].surface + self.morphs[i+1].surface
        return ''

    def get_word_conversion_surface(self, pos, s):
        result = ''
        for morph in self.morphs:
            if morph.pos == pos:
                result += s
            elif morph.pos != '記号':
                result += morph.surface
        return result


def get_chunks_list(path):
    sentences = []
    chunks = {}
    with open(path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.rstrip()
            if line == 'EOS':
                if len(chunks) > 0:
                    sentence = [chunks[key] for key in sorted(chunks.keys())]
                    sentences.append(sentence[:])
                    chunks = {}
            elif line[0] == '*':
                s = line.split()
                current_num = int(s[1])
                dst = int(s[2][:-1])
                if current_num not in chunks:
                    chunks[current_num] = Chunk([], dst, [])
                chunks[current_num].dst = dst
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk([], -1, [])
                    chunks[dst].srcs.append(current_num)
            else:
                elements = re.split('[\t,]', line)
                morph = Morph(elements[0], elements[7],
                              elements[1], elements[2])
                chunks[current_num].morphs.append(morph)
    return sentences


if __name__ == "__main__":
    path = 'neko.txt.cabocha'
    sentences = get_chunks_list(path)
    for i, chunk in enumerate(sentences[7]):
        print(f'{i}:{chunk}')
