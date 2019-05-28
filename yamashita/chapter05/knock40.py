import re


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f'surface:{self.surface}\tbase:{self.base}\tpos:{self.pos}\tpos1:{self.pos1}'


def get_morpheme_list(path):
    sentences = []
    morphemes = []
    with open(path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.rstrip()
            if line == 'EOS':
                if len(morphemes) > 0:
                    sentences.append(morphemes[:])
                    morphemes.clear()
            elif line[0] == '*':
                pass
            else:
                splited = re.split('[\t,]', line)
                morpheme = Morph(splited[0], splited[7],
                                 splited[1], splited[2])
                morphemes.append(morpheme)

    return sentences


if __name__ == "__main__":
    path = 'neko.txt.cabocha'
    sentences = get_morpheme_list(path)
    # for sentence in sentences[:20]:
    #     for morph in sentence:
    #         print(morph)
    for morpheme in sentences[2]:
        print(morpheme)
