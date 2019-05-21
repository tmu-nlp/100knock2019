
import MeCab
def fileopen ():
    inputname = r"\Users\Koya\Documents\Lab\neko.txt"
    outputname = r"\Users\Koya\Documents\Lab\neko.txt.mecab"
    with open( inputname, mode = "r",encoding="utf-8")as inputfile:
        with open( outputname, mode = "w",encoding="utf-8")as outputfile:
            outputfile.write(MeCab.Tagger("-Ochasen").parse(inputfile.read()))
            
    
fileopen()