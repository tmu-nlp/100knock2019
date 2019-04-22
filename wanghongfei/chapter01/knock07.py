def temp(x, y, z):
    seq = '%d時の%sは%.1f' % (x, y, z)
    return seq


x = 12
y = '気温'
z = 22.4
print(temp(x, y, z))
