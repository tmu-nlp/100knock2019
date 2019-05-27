from knock41 import importchunklists


def kakariukepath(clist: list):

    with open('koubunki.txt', 'w+', encoding='utf-8') as f:

        # 1文ずつ
        for chunks in clist:

            # １文節ずつ
            for chunk in chunks:
                if not chunk.hasnoun():
                    continue

                # 構文木Chunkのリストを作る。
                chunklist = [chunk]

                while True:
                    # 係り先がなくなったらおしまい
                    if chunklist[-1].dst == -1:
                        line = chunk.text
                        for i in range(1, len(chunklist)):
                            line += ' -> ' + chunklist[i].text
                        print(line, file=f)
                        break
                    # 係り先があれば追加
                    else:
                        chunklist.append(chunks[chunklist[-1].dst])


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)
    kakariukepath(clist)


if __name__ == '__main__':
    main()
