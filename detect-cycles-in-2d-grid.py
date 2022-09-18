class Solution:
    def DFS(self, grid, i, j, m, n, v, prev):
        v.add((i, j))
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == grid[i][j] and (x, y) != prev:
                if (x, y) not in v:
                    if self.DFS(grid, x, y, m, n, v, (i, j)):
                        return True
                else:
                    return True
        return False
    
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        v = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in v:
                    if self.DFS(grid, i, j, m, n, v, (None, None)):
                        return True
        return False