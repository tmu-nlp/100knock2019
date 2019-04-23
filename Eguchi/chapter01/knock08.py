##与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
##英小文字ならば(219 - 文字コード)の文字に置換
##その他の文字はそのまま出力
##この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher (sentence):
    words=list(sentence)   
    count = 0

    for i in words:
        if words[count].islower()==True:
            wordcode =  ord(words[count])
            words[count] = chr(219 - wordcode)          
        count+=1

    words = "".join(words)
    print(words)

    

    words = list(words)
    count=0
    for i in words:
        if words[count].islower()==True:
            wordcode = ord(words[count])
            words[count] = chr( 219 - wordcode)
        count +=1
    words = "".join(words)
    print(words)



sentence = input()
cipher(sentence)



