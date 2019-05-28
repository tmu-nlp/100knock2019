class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
   
    def __str__(self):
        return "surface: '{}', base: '{}', pos: '{}', pos1: '{}'"\
                .format(self.surface, self.base, self.pos, self.pos1)

def get_morph(file_name):
    file = open(file_name, "r").readlines()
    sentences_list = []
    words_list = []
    for line in file:
        if line[0] == "*":
            pass
        elif "EOS" in line:
            sentences_list.append(words_list)
            words_list = []
        else:
            line = line.strip().replace("\t", ",").split(",")
            morph = Morph(line[0],line[7],line[1],line[2])
            words_list.append(morph)
    return sentences_list

if __name__ == "__main__":
    file_name = "./neko.txt.cabocha"
    sentences = get_morph(file_name) 
    for morph in sentences[2]:
        print(morph)