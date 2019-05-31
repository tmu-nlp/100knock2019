import re


def segmentation(fin: str, fout: str):
    with open(fin, 'r', encoding='utf-8') as i_f, \
         open(fout, 'w+', encoding='utf-8') as o_f:

        for line in i_f:

            # 空行は無視
            if line != '\n':

                line = line.rstrip()

                ptn = r'''
                [.;:?!] # [.;:?!]のうちのどれか
                \s+     # 空白
                (?=[A-Z])   # 次の文字が大文字
                '''
                ls = re.compile(ptn).split(line)

                for l in ls:
                    print(l, file=o_f)


def main():
    fin = 'nlp.txt'
    fout = '50.txt'
    segmentation(fin, fout)


if __name__ == '__main__':
    main()
