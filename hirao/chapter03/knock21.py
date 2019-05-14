from knock20 import get_text

for s in get_text().split("\n"):
    # "Category"が1つ以上存在するものを表示する
    if s.find("Category") > 0:
        print(s)
