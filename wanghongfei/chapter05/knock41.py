class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
   
    def __str__(self):
        return "surface: '{}', base: '{}', pos: '{}', pos1: '{}'"\
                .format(self.surface, self.base, self.pos, self.pos1)

class Chunk(object):
    def __init__(self, morphs, dst, src):
        self.morphs = morphs
        self.dst = dst
        self.src = src
    
    def __str__(self):
        return "morphs:'{}', dst:'{}', src:'{}'"\
               .format(self.morphs, self.dst, self.src)

def get_src_num(sentence, chunk_num):
    src_num_list = []
    for item in sentence:
        if "*" in item[0]:
            item = item.split(" ")
            if item[2].strip("D") == str(chunk_num):
                src_num_list.append(item[1])
    return src_num_list

def get_chunk(file_name):
    file = open(file_name,"r").readlines()
    chunks_list = []
    sentence_info =[] #全文の情報がほしい
    article = []
    for line in file:
        if "EOS" not in line:
            sentence_info.append(line)#１文が終わり、分析開始
        if "句点" in line:    
            for item in sentence_info: #文節単位で
                if "*" in item[0]:
                    chunk = item.split(" ")
                    dst = chunk[2].strip("D")
                    src = get_src_num(sentence_info, chunk[1])
                    morph_list = []
                    for morph in sentence_info[sentence_info.index(item)+1:]: #次の文節までの形態素を抽出
                        if "*" not in morph[0]:
                            morph_item = morph.strip().replace("\t", ",").split(",")
                            morph_instance = [morph_item[0],morph_item[7],morph_item[1],morph_item[2]]
                            morph_list.append(morph_instance)
                        else:
                            break
                    chunk = Chunk(morph_list, dst, src)
                    chunks_list.append(chunk)
            article.append(chunks_list)
            chunks_list = []
            sentence_info = [] #１文の分析が完了
    return article

if __name__ == "__main__":
    file_name = "./neko.txt.cabocha"
    chunks = get_chunk(file_name)
    for i in chunks[7]:
        print(i)







