s = input()

b = []
r = []
k = -1

for i, c in enumerate(s):
    if c == 'B':
        b.append(i)
    if c == 'R':
        r.append(i)
    if c == 'K':
        k = i

print("Yes" if b[0] % 2 != b[1] % 2 and r[0] < k < r[1] else "No")