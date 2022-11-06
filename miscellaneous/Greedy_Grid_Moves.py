import sys

sys.setrecursionlimit(10**6)

t = int(input())

def getminval(grid, i, j, m, n, becky, cache):
    if (i, j) == (m - 1, n - 1):
        return grid[i][j]
    key = (becky, i, j)
    if key in cache:
        return cache[key]
    if i == m - 1:
        curr = getminval(grid, i, j + 1, m, n, not becky, cache)
        res = max(grid[i][j], curr)
        cache[key] = res
        return res
    if j == n - 1:
        curr = getminval(grid, i + 1, j, m, n, not becky, cache)
        res = max(grid[i][j], curr)
        cache[key] = res
        return res
    if becky:
        a = max(grid[i][j], getminval(grid, i + 1, j, m, n, not becky, cache))
        b = max(grid[i][j], getminval(grid, i, j + 1, m, n, not becky, cache))
        res = min(a, b)
        cache[key] = res
        return res
    else:
        if grid[i + 1][j] > grid[i][j + 1]:
            curr = getminval(grid, i + 1, j, m, n, not becky, cache)
            res = max(grid[i][j], curr)
            cache[key] = res
            return res
        else:
            curr = getminval(grid, i, j + 1, m, n, not becky, cache)
            res = max(grid[i][j], curr)
            cache[key] = res
            return res

for _ in range(t):
    m, n = map(int, input().split())
    grid = []
    for __ in range(m):
        grid.append(list(map(int, input().split())))
    print(getminval(grid, 0, 0, m, n, True, {}))