hightemp = open('./col1.txt').readlines()
set_prov = set() 
for prov in hightemp:
    set_prov.add(prov.strip("\n"))
print(set_prov)

