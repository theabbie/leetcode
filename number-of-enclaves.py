class Solution:
    def dfs(self, grid, i, j, m, n, visited):
        visited.add((i, j))
        grid[i][j] = 0
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited:
                self.dfs(grid, x, y, m, n, visited)
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        boundary = set()
        for i in range(m):
            boundary.add((i, 0))
            boundary.add((i, n - 1))
        for i in range(n):
            boundary.add((0, i))
            boundary.add((m - 1, i))
        globalvisited = set()
        ctr = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    currvisited = set()
                    self.dfs(grid, i, j, m, n, currvisited)
                    if len(set.intersection(currvisited, boundary)) == 0:
                        ctr += len(currvisited)
        return ctr