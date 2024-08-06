class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        graph = [[] for _ in range(m * n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                        graph[n * i + j].append((n * x + y, grid[x][y]))
        @lru_cache(maxsize = None)
        def mpath(i, used):
            res = 0
            for j, w in graph[i]:
                if not used & (1 << j):
                    res = max(res, w + mpath(j, used | (1 << j)))
            return res
        return max(grid[i // n][i % n] + mpath(i, 1 << i) for i in range(m * n))