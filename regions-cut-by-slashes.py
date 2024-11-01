from collections import *

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                for x, y, s, p in [(i, j - 1, 3, 1), (i - 1, j, 0, 2), (i, j + 1, 1, 3), (i + 1, j, 2, 0)]:
                    if 0 <= x < n and 0 <= y < n:
                        graph[(i, j, s)].append((x, y, p))
                        graph[(x, y, p)].append((i, j, s))
                ops = []
                if grid[i][j] == '/' or grid[i][j] == ' ':
                    ops.extend([(2, 1), (3, 0)])
                if grid[i][j] == '\\' or grid[i][j] == ' ':
                    ops.extend([(0, 1), (2, 3)])
                for x, y in ops:
                    graph[(i, j, x)].append((i, j, y))
                    graph[(i, j, y)].append((i, j, x))
        res = 0
        v = set()
        def dfs(x):
            v.add(x)
            for y in graph.get(x, []):
                if y not in v:
                    dfs(y)
        for x in graph:
            if x not in v:
                res += 1
                dfs(x)
        return res