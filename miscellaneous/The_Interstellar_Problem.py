t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    vals = [[0, 0] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            vals[j][0] = 2 * vals[j][0] + grid[i][j]
            vals[j][1] = 2 * vals[j][1] + 1 - grid[i][j]
    for i in range(m):
        for j in range(n):
            if vals[j][1] > vals[j][0]:
                grid[i][j] = 1 - grid[i][j]
    zctr = [0] * m
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                zctr[i] += 1
    for i in range(m):
        for j in range(n):
            if zctr[i] * 2 > n:
                grid[i][j] = 1 - grid[i][j]
    vals = [0] * n
    for i in range(m):
        for j in range(n):
            vals[j] = 2 * vals[j] + grid[i][j]
    print(sum(vals))