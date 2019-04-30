import linecache
def n_lines_print(s: str, num: int):
    for i in range(1, num + 1):
        print(linecache.getline(s, i), end = "")

if __name__ == "__main__":
    import sys
    n_lines_print("hightemp.txt", sys.argv[1])