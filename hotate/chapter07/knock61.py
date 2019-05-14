import plyvel


def search_area(name: str) -> str:
    db = plyvel.DB('./db_knock60/')
    try:
        area = db.get(name.encode('utf-8')).decode('utf-8')
    except AttributeError:
        area = 'The artist name is not registered.'
    db.close()
    return area


if __name__ == '__main__':
    while True:
        input_text = input('Please enter an artist name. (quit command: "q")\n')
        if input_text == 'q':
            break
        else:
            area = search_area(input_text)
            print(f'area : {area}')
            print('-'*100)
