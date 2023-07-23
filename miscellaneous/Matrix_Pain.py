from collections import defaultdict

t = int(input())

M = 10 ** 9 + 7

for _ in range(t):
    n, m, k = map(int, input().split())
    rows = defaultdict(lambda: 1)
    cols = defaultdict(lambda: 1)
    for _ in range(k):
        q, x, v = map(int, input().split())
        if q == 0:
            rows[x] *= v
            rows[x] %= M
        if q == 1:
            cols[x] *= v
            cols[x] %= M
    currsum = 0
    colsum = m * (m + 1) // 2
    csum = m
    rowsum = n * (n + 1) // 2
    rsum = n
    for c in cols:
        colsum += c * (cols[c] - 1)
        csum += cols[c] - 1
        colsum %= M
        csum %= M
    for r in rows:
        rowsum += r * (rows[r] - 1)
        rsum += rows[r] - 1
        rowsum %= M
        rsum %= M
    currsum += (rowsum - rsum) * m * csum + rsum * colsum
    currsum %= M
    print(currsum)