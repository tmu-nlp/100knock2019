from knock41 import importchunklists
from itertools import combinations


def kakariukepath(clist: list):

    with open('kakariuke.txt', 'w+', encoding='utf-8') as f:

        # 1文ずつ
        for chunks in clist:
            # 名詞句だけ抜き取り
            np_chunks = [chunk for chunk in chunks if chunk.hasnoun() is True]

            # X候補とY候補の取り出し: xy = [xchunk, ychunk]
            for xy in combinations(np_chunks, 2):
                # Xの係り先、その係り先、…を入れるリスト
                xlist = [xy[0]]

                # まずXの係り先について調べる
                while True:
                    # Yが見つかればおしまい
                    if chunks[xlist[-1].dst] == xy[1]:
                        # print(xlist[0].returnnoun())
                        print('X'
                              + ''.join([morph.surface for morph
                                         in xlist[0].morphs
                                         if morph.pos != '名詞'])
                              + '->'+''.join([chunk.text+'->' for chunk
                                              in xlist[1:]])
                              + 'Y',
                              file=f)
                        # print('|'+chunks[xlist[-1].dst].text)
                        break
                    # 係り先がなくなったらおしまい
                    elif xlist[-1].dst == int(-1):
                        # Yの係り先について調べる
                        ylist = [xy[1]]
                        while True:
                            # 係り先がXの根になったらおしまい
                            if chunks[ylist[-1].dst] == xlist[-1]:
                                print('X'+''.join([morph.surface for morph
                                                   in xlist[0].morphs
                                                   if morph.pos != '名詞'])+'|'
                                      + 'Y'+''.join([morph.surface for morph
                                                     in ylist[0].morphs
                                                     if morph.pos != '名詞'])
                                      + ('->'+''.join([chunk.text+'->'
                                                      for chunk
                                                      in ylist[1:]])
                                         if (ylist[1:] != []) else '')
                                      + '|'+chunks[ylist[-1].dst].text,
                                      file=f)

                                break
                            # 係り先がXの根でない場合はリストに追加
                            else:
                                ylist.append(chunks[ylist[-1].dst])
                        break

                    # Yでない係り先があればリストに追加
                    else:
                        # xlistの一番後ろの係り先をxlistに追加
                        xlist.append(chunks[xlist[-1].dst])


def main():
    path = 'neko.txt.cabocha'
    clist = importchunklists(path)
    kakariukepath(clist)


if __name__ == '__main__':
    main()
