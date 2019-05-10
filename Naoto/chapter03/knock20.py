with open("jawiki-country.json", mode = "r") as input_,\
    open("jawiki-イギリス.json", mode = "w") as output_:
    for line in input_:
    #     sentences = list(line.split("。"))
    #     for sentence in sentences:
        if "国\n|略名 =イギリス" in line:
            output_.write(line)
    print(line)