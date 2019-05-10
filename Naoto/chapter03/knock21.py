def category_line(s: str) -> list:
    with open(s) as fp:
        json_data = fp.readline()
        list_ = []
        while json_data:
            if "===" in json_data:
                list_.append(json_data.strip())
            json_data = fp.readline()
    return list_

print(category_line("jawiki-イギリス.json"))