import math

def count(n):
    vals = []
    for i in range(1, 10 * n + 1):
        if (i ^ n) < n:
            vals.append(i)
    res = []
    m = len(vals)
    i = 0
    while i < m:
        ctr = 1
        while i < m - 1 and vals[i + 1] == vals[i] + 1:
            i += 1
            ctr += 1
        res.append((vals[i] - ctr + 1, vals[i]))
        i += 1
    return res

for i in range(7091, 7091):
    x = i
    beg = 1
    while x % 2 == 0:
        x = x // 2
        beg *= 2
    print(i, (beg, 2 ** (1 + int(math.log2(i))) - 1), count(i))

print(count(101))