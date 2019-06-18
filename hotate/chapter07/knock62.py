import plyvel


def main():
    db = plyvel.DB('./db_knock60/')
    sum_ = sum(1 for name, area in db if area == b'Japan')
    db.close()
    print(sum_)


if __name__ == '__main__':
    main()
