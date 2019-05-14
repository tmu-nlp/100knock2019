import plyvel


def sum_japan():
    db = plyvel.DB('./db_knock60/')
    sum_ = sum(1 for name, area in db if area == b'Japan')
    db.close()
    return sum_


if __name__ == '__main__':
    print(sum_japan())
