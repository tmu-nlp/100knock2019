Patrol_car = "パトカー"
taxi = "タクシー"
ans = ''.join([str1 + str2 for str1, str2 in zip(Patrol_car, taxi)])
# ans = ''.join(str1 + str2 for str1, str2 in zip(Patrol_car, taxi))

print("ans = %s" % ans)