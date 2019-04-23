def n_gram1(str,num):
    list = []
    for i in range(len(str)-num+1):
        list.append(str[i:i+num])

    return list

x = "paraparaparadise"
y = "paragraph"
x_list = set(n_gram1(x,2))
y_list = set(n_gram1(y,2))

list1 = x_list | y_list
list2 = x_list & y_list
list3 = x_list - y_list

def serch_se(list):
    if "se" in list:
        a = "含む"
        return a
    else:
        a = "含まない"
        return a



print("X"+str(x_list))
print("Y"+str(y_list))
print("和集合"+str(list1))
print("積集合"+str(list2))
print("差集合(x-y)"+str(list3))
print("Xがseを"+serch_se(x_list))
print("Yがseを"+serch_se(y_list))
