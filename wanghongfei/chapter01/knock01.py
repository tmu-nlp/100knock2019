str1 = "パタトクカシーー"
str2 = ''
for key, val in enumerate(str1):
    if key % 2 != 0:
        str2 = str2 + val
print(str2)
#  enumerate() is a function which returns a tuple containing 
# a count and the value obtained from iterating over iterable.
