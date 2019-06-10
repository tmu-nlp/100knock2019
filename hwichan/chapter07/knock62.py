import leveldb


def main():
    db = leveldb.LevelDB('knock60')
    search_area = input('活動場所 : ')

    n = 0
    for name, area in db.RangeIter():
        if area.decode() == search_area:
            n += 1
            print(name.decode().split('_')[0])

    print(n)


if __name__ == '__main__':
    main()

