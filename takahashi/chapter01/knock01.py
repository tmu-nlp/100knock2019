# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

def extract_odd_letters(target: str) -> str:
    return (target[1::2])

if __name__ == "__main__":
    print(extract_odd_letters("パタトクカシーー"))