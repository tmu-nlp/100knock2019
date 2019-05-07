letter1 = "パトカー"
letter2 ="タクシー"
ans = ""

for i in range(4):
    ans = ans + letter1[i] + letter2[i]
    
print(ans)

##zip_longestを使って、単語数の最大を取る.fillvalueで不足分を補う