str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str2 = str1.strip(".").replace(',', '')  # Delete ',' and '.' .
w_list = str2.split(' ')  # Divide the string by space, and then the store obtained words in list.
print(w_list)
w_len = []
for word in w_list:
    w_len.append(len(word)) 
print(w_len)





