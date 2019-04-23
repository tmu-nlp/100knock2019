# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

def connect_alternately(target1: str, target2: str) -> str:
    result = ""
    for c1, c2 in zip(target1, target2):
        result += c1 + c2
    return result

if __name__ == "__main__":
    print(connect_alternately("パトカー", "タクシー"))