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
    for i, line in enumerate(sentence_extraction()):
        if i == 10:
            break
        words = line.strip('\n').split(' ')
        for word in words:
            if word == '':
                continue
            print(word)
        print('\n')


if __name__ == '__main__':
    main()
