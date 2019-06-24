import re


def main():
    with open('enwiki-20150112-400-r100-10576.txt', 'r', encoding='utf-8') as input_file, \
         open('out.txt', 'w', encoding='utf-8') as out_file:
        text = []

        for line in input_file:
            line = line.strip()
            words = []
            for w in line.split(' '):
                word = w.strip('.,!?;:()[]\'"')
                if len(word) > 0:  # 空文字ではなかったらwordsに追加
                    words.append(word)
            text.append(' '.join(words))

        out_file.write('\n'.join(text))


if __name__ == "__main__":
    main()
