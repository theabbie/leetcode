from collections import *

t = int(input())

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                parent_a, parent_b = parent_b, parent_a
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]

def check(grid, m, n):
    key = lambda i, j: n * i + j
    dsu = DSU(m * n)
    for i in range(m):
        for j in range(n):
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[i][j] == grid[x][y] == "W":
                    dsu.union(key(i, j), key(x, y))
    groups = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "W":
                groups[dsu.find(key(i, j))].append((i, j))
    extras = defaultdict(int)
    res = 0
    for g in groups:
        extra = set()
        for i, j in groups[g]:
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == ".":
                    extra.add((x, y))
        if len(extra) == 1:
            extras[min(extra)] += len(groups[g])
            res = max(res, extras[min(extra)])
    return res

for xx in range(t):
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(input())
    print(f"Case #{xx + 1}: {check(grid, m, n)}")