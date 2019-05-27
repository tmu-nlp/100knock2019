import CaboCha
c = CaboCha.Parser()


def read_file(filename: str) -> str:
    c_list = []
    with open(filename, 'r') as f:
        for line in f:
            tree = c.parse(line)
            c_list.append(tree.toString(CaboCha.FORMAT_LATTICE))

    return ''.join(c_list)


def write_file(text: str, filename: str):
    with open(filename, 'w') as f:
        f.write(text)


def main():
    write_file(read_file('neko.txt'), 'neko.txt.cabocha')
    

if __name__ == '__main__':
    main()
