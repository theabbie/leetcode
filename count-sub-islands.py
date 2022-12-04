class Solution:
    def DFS(self, grid, i, j, m, n, v):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and (i, j) not in v:
            v.add((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                self.DFS(grid, x, y, m, n, v)
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        res = 0
        v = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in v:
                    currv = set()
                    self.DFS(grid2, i, j, m, n, currv)
                    subisle = True
                    for x, y in currv:
                        if grid1[x][y] == 0:
                            subisle = False
                            break
                    if subisle:
                        res += 1
                    v.update(currv)
        return res