import linecache
def n_lines_print_back(s: str, n: str):
    with open(s, "r") as ipt:
        l = len(list(ipt))
        for i in reversed(range(l - int(n), l)):
            print(linecache.getline(s, i), end = "")


if __name__ == "__main__":
    import sys
    n_lines_print_back("hightemp.txt", sys.argv[1])