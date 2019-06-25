class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1


one_sent = []
surf = "abc"
items = [0,1,2,3,4,5,6,7]

one_sent.append(Morph(surf, items[6], items[0], items[1]))
print(Morph(surf, items[6], items[0], items[1]))
print(one_sent)
print(Morph(surf, items[6], items[0], items[1]).surface)
for item in one_sent:
    print ('surface=%s\tbase=%d\tpos=%d\tpos1=%d' % (item.surface, item.base, item.pos, item.pos1) )

"""
all_sent = []

with open('neko.txt.cabocha', encoding='utf-8') as cabochaed:
    for line in cabochaed:
        if line[0] == "*" :
            next
        if "\t" in line:
            item = line.strip().split("\t")
            try: # 一文字目が空白で始まるものがうまく処理できなかったので、try - exceptを使うことにした
                surf = item[0]
                items = item[1].split(",")
            except IndexError: # 一文字目が空白だとIndexErrorを起こすみたい
                next
            if not item == ['記号,空白,*,*,*,*,\u3000,\u3000,']: # 空白の箇所の処理, \u3000は空白、ここはかなりアドホックな処理をしている
                one_sent.append(Morph(surf, items[6], items[0], items[1]))
        elif "EOS" in line:
            if len(one_sent) > 0:
                all_sent.append(one_sent)
            one_sent = []

for item in all_sent[3]:
    print ('surface=%s\tbase=%s\tpos=%s\tpos1=%s' % (item.surface, item.base, item.pos, item.pos1) )
        """