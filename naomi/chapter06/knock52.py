from stemming.porter2 import stem


def segment_words(fin: str, fout: str):
    with open(fin, 'r', encoding='utf-8') as i_f, \
         open(fout, 'w+', encoding='utf-8') as o_f:

        for word in i_f:
            word = word.rstrip('\n').rstrip(',.;:?!')
            stemed_word = stem(word)

            print(stemed_word, file=o_f)


def main():
    fin = '51.txt'
    fout = '52.txt'
    segment_words(fin, fout)


if __name__ == '__main__':
    main()
