
def segment_words(fin: str, fout: str):
    with open(fin, 'r', encoding='utf-8') as i_f, \
         open(fout, 'w+', encoding='utf-8') as o_f:

        for line in i_f:
            # 空行は無視
            if line != '\n':

                words = line.rstrip().split(' ')

                for word in words:
                    print(word, file=o_f)


def main():
    fin = '50.txt'
    fout = '51.txt'
    segment_words(fin, fout)


if __name__ == '__main__':
    main()
