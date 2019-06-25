import CaboCha
path = r"\Users\Koya\Documents\Lab\neko.txt"
with open(path, encoding= "utf-8") as f:
    cabocha = CaboCha.Parser()
    for line in f:
        After_CaboCha = cabocha.parse(line)
        with open(r"\Users\Koya\Documents\Lab\neko.txt.cabocha",mode="w",encoding="utf-8" ) as outputfile:
            print(After_CaboCha.toString(CaboCha.FORMAT_LATTICE))
            outputfile.write(After_CaboCha.toString(CaboCha.FORMAT_LATTICE))


