Patrol_car = "パトカー"
taxi = "タクシー"
ans = ""
for str1, str2 in zip(Patrol_car, taxi):
    ans += str1 + str2

print("ans = %s" % ans)

#zip, zip_longest