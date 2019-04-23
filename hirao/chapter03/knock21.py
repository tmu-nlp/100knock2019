from knock20 import get_json

for s in get_json().split("\n"):
    if s.find("Category") >= 0:
        print(s)
