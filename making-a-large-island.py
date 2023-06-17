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

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dsu = DSU(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        dsu.union(m * i + j, m * x + y)
        res = max(dsu.size)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                sizes = {}
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        sizes[dsu.find(m * x + y)] = dsu.size[dsu.find(m * x + y)]
                res = max(res, 1 + sum(sizes.values()))
        return res