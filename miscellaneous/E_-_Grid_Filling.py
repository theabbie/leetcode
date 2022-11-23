from collections import Counter

m, n, k, h, w = map(int, input().split())

grid = []
total = [0] * (k + 1)

for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)
    for el in row:
        total[el] += 1

ctr = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        for a in range(1, k + 1):
            ctr[i][j][a] = ctr[i][j - 1][a] + ctr[i - 1][j][a] - ctr[i - 1][j - 1][a]
        ctr[i][j][grid[i - 1][j - 1]] += 1

for i in range(m - h + 1):
    for j in range(n - w + 1):
        curr = 0
        for a in range(1, k + 1):
            c = ctr[i + h][j + w][a]
            l = ctr[i + h][j][a]
            t = ctr[i][j + w][a]
            s = ctr[i][j][a]
            if total[a] > c - l - t + s:
                curr += 1
        print(curr, end = " ")
    print()