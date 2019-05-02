import sys
my_file = open(sys.argv[1], "r")

ans = 0

for line in my_file:
    ans += 1

my_file.close()

print(ans)
