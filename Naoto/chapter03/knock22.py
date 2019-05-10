def get_category_names(s: str) -> list:
    from collections import defaultdict

    with open(s) as fp:
        json_data = fp.readline()
        list_ = []
        while json_data:
            str_ = ""
            if "Category" in json_data:
                for i in range(11, len(json_data)):
                    if json_data[i] == "]":
                        break
                    else:
                        str_ += json_data[i]
                list_.append(str_)
            json_data = fp.readline()
    
    return list_
    
if __name__ == "__main__":
    print(get_category_names("jawiki-イギリス.json"))