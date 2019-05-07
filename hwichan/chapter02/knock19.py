import sys


def read_file(filename: str) -> list:
    cal1_count = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            cal1_count[words[0]] = cal1_count.get(words[0], 0) + 1

    return cal1_count

#lambda 引数:処理 で無名関数を作成できる、
def main():
    cal1_count = read_file(sys.argv[1])
    cal1_count = sorted(cal1_count.items(), key=lambda x: x[1], reverse = True) # (地域名, 出現頻度)
    cal1_list = list(map(lambda x: f'{x[1]} {x[0]}', cal1_count))
    print('\n'.join(cal1_list))

if  __name__  ==  '__main__':
    main()

# A)  cut -f 1 hightemp.txt | sort -n | uniq -c | sort -r
