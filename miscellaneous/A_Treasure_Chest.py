n = int(input())

s = input()

valid = False

ctr = 0

for c in s:
    if c == "|":
        ctr += 1
    if c == "*":
        if ctr == 1:
            valid = True
            break

print("in" if valid else "out")