def transfer_txt_to_list(txt: str, op: str) -> list:
    with open(txt, op) as input:
        lis = [character for line in input for character in line]
    return lis

if __name__ == "__main__":
    col1_list = transfer_txt_to_list("col1.txt", "r")
    col2_list = transfer_txt_to_list("col2.txt", "r")
    with open("col1_2_merge_13.txt", "w") as col1_2_merge_13:
        count = 0
        for i in range(len(col1_list)):
            if col1_list[i] != "\n":
                col1_2_merge_13.write(col1_list[i])
                # print(col1_list[i], end = "")
            else:
                col1_2_merge_13.write("\t")
                # print("\t", end = "")
                while True:
                    col1_2_merge_13.write(col2_list[count])
                    # print(col2_list[count], end = "")
                    if col2_list[count] == "\n":
                        count += 1
                        break
                    count += 1

