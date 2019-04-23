def temp(x,y,z):
    str = '{0}時の{1}は{2}'.format(x,y,z) #x->{0} y->{1} z->{2} format:文字列にあった方で挿入してくれる
    return str

x = 12
y = "気温"
z = 22.4

print(temp(x,y,z))
