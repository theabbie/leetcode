class Solution:
    def minCost(self, grid, moveCost, i, j, m, n):
        if i == m - 1:
            return grid[i][j]
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        mincost = float('inf')
        for col in range(n):
            curr = self.minCost(grid, moveCost, i + 1, col, m, n)
            mincost = min(mincost, grid[i][j] + moveCost[grid[i][j]][col] + curr)
        self.cache[(i, j)] = mincost
        return mincost
    
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.cache = {}
        mincost = float('inf')
        for j in range(n):
            curr = self.minCost(grid, moveCost, 0, j, m, n)
            mincost = min(mincost, curr)
        return mincost