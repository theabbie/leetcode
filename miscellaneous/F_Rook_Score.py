from collections import defaultdict

n = int(input())

rows = defaultdict(int)
cols = defaultdict(int)
exist = {}
rowvals = defaultdict(set)

for _ in range(n):
    r, c, x = map(int, input().split())
    rows[r] += x
    cols[c] += x
    exist[(r, c)] = x
    rowvals[r].add(c)

colvals = sorted(cols.items(), key = lambda p: -p[1])

res = 0

for r, c in exist:
    res = max(res, rows[r] + cols[c] - exist.get((r, c), 0))

for r in rows:
    for c, score in colvals:
        if c not in rowvals[r]:
            res = max(res, rows[r] + score)
            break

print(res)