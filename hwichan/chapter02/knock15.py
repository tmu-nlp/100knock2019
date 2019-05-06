import sys


def read_file(filename: str):
    with open(filename, "r") as file:
        return file.readlines()


def main():
    N = sys.argv[1]
    line = read_file(sys.argv[2])
    # type(N) == <class 'str'> コマンドライン引数はstr型
    print(''.join(line[-int(N):]))

if  __name__  ==  '__main__':
    main()

#https://eng-entrance.com/linux-command-tail
# A : tail -n N filename
