from knock30 import get_morph
result = get_morph("./chapter04/neko.txt.mecab")
nouns = ""
for sentence in result:
    for morph in sentence:
        if "名詞" == morph["品詞"]:
            nouns = nouns + morph["基本形"]
        else :
            if len(nouns) > 0:
                print(nouns)
                nouns = ""
        
        
            
