with open("jawiki-イギリス.json", "r") as イギリス:
    for line in イギリス:
        if "Category" in line:
            print(line, end="")