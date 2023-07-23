n = int(input())

s = input()

g = f = p = 0

for c in s:
    if c == 'o':
        g += 1
    if c == '-':
        f += 1
    if c == 'x':
        p += 1

print("Yes" if g > 0 and p == 0 else "No")