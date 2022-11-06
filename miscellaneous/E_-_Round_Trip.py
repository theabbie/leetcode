from collections import defaultdict

m, n = map(int, input().split())

grid = []

for _ in range(m):
    grid.append(input())

v = set()

beg = None

for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            beg = (i, j)
        elif grid[i][j] == "#":
            v.add((i, j))

def getnb(p, m, n):
    for i, j in [(p[0] - 1, p[1]), (p[0], p[1] - 1), (p[0] + 1, p[1]), (p[0], p[1] + 1)]:
        if 0 <= i < m and 0 <= j < n:
            yield (i, j)

v.add(beg)

def DFS(curr, m, n, v, d):
    for i, j in getnb(curr, m, n):
        if grid[i][j] == "S" and d >= 4:
            return True
        if (i, j) not in v:
            v.add((i, j))
            if DFS((i, j), m, n, v, d + 1):
                return True
            v.remove((i, j))
    return False

print("Yes" if DFS(beg, m, n, v, 0) else "No")