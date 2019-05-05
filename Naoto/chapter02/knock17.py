import sys

row = list(sys.stdin)
set_1 = set()
for character in row:
    set_1.add(character)
print(sorted(set_1))
