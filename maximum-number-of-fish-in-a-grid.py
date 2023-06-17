class Solution:
    def DFS(self, grid, i, j, m, n, v):
        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in v and grid[x][y] > 0:
                v.add((x, y))
                self.DFS(grid, x, y, m, n, v)
    
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        v = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i, j) not in v:
                    curr = {(i, j)}
                    self.DFS(grid, i, j, m, n, curr)
                    currfish = 0
                    for x, y in curr:
                        currfish += grid[x][y]
                    res = max(res, currfish)
                    v.update(curr)
        return res