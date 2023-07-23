n = int(input())

s = input()

vals = []

res = -1

i = 0

while i < n:
    ctr = 1
    while i < n - 1 and s[i] == s[i + 1]:
        ctr += 1
        i += 1
    vals.append((s[i], ctr))
    i += 1

for i in range(len(vals)):
    if vals[i][0] == 'o':
        if i > 0 or i < len(vals) - 1:
            res = max(res, vals[i][1])

print(res)