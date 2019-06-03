import re


def sentence_extraction():
    pattern = re.compile(r'''
        (
            ^.*?                # 非貪欲
            [\.|;|:|\?|!]       # . or ; or : or ? or !
        )
        \s                      # 空白
        (
            [A-Z].*             # 英大文字
        )
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

    with open('nlp.txt', 'r') as f:
        for line in f:
            line = line.strip('\n')
            while True:
                if line == '':
                    break

                s = pattern.match(line)
                if s:
                    yield s.group(1)
                    line = s.group(2)
                else:  # マッチしないということは最後までが１文
                    yield line
                    break


def main():
    for line in sentence_extraction():
        print(line)


if __name__ == '__main__':
    main()
