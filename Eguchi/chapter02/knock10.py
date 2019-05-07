

filename = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02\hightemp.txt"
file = open(filename, "r",encoding="utf-8"  )

print( len(file.readlines()))

file.close()
