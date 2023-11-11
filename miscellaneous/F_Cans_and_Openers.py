n, m = map(int, input().split())

vals = [[], [], []]

for _ in range(n):
    a, b = map(int, input().split())
    vals[a].append(b)

vals[0].sort(reverse = True)
vals[1].sort(reverse = True)
vals[2].sort(reverse = True)

pfree = [0] * (len(vals[0]) + 1)

for i in range(len(vals[0])):
    pfree[i + 1] += pfree[i] + vals[0][i]

p = [0] * (len(vals[1]) + 1)

for i in range(len(vals[1])):
    p[i + 1] += p[i] + vals[1][i]

res = 0

openers = 0

for i in range(len(vals[2]) + 1):
    rem = m - i
    for x in range(min(rem, len(vals[0])) + 1):
        res = max(res, pfree[x] + p[min(openers, rem - x, len(vals[1]))])
    if i < len(vals[2]):
        openers += vals[2][i]

print(res)