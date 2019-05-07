import sys


def read_file(filename: str) -> list:
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.split('\t')[0])

    return lines


def main():
    cal1_list = set(read_file(sys.argv[1])) #set : 配列を集合にする
    print('\n'.join(sorted(cal1_list)))

if  __name__  ==  '__main__':
    main()

#https://eng-entrance.com/linux-command-split
# A : sort -u cal1.txt
