from bisect import bisect_left

t = int(input())

res = []

for _ in range(t):
    n = int(input())
    curr = 0
    row = []
    col = []
    pp = []
    nn = []
    points = []
    for __ in range(n):
        a, b = map(int, input().split())
        points.append((a, b))
        row.append(a)
        col.append(b)
        pp.append(a + b)
        nn.append(a - b)
    row.sort()
    col.sort()
    pp.sort()
    nn.sort()
    rowctr = [0] * len(row)
    colctr = [0] * len(col)
    ppctr = [0] * len(pp)
    nnctr = [0] * len(nn)
    for a, b in points:
        curr += rowctr[bisect_left(row, a)] + colctr[bisect_left(col, b)] + ppctr[bisect_left(pp, a + b)] + nnctr[bisect_left(nn, a - b)]
        rowctr[bisect_left(row, a)] += 1
        colctr[bisect_left(col, b)] += 1
        ppctr[bisect_left(pp, a + b)] += 1
        nnctr[bisect_left(nn, a - b)] += 1
    res.append(curr * 2)

print(*res)