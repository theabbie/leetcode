class Solution:
    def getmax(self, grid, i, x, y):
        if i >= len(grid) - 1:
            return 0
        key = (i, x, y)
        if key in self.cache:
            return self.cache[key]
        res = 0
        for a in range(x - 1, x + 2):
            for b in range(y - 1, y + 2):
                if 0 <= a < len(grid[0]) and 0 <= b < len(grid[0]):
                    score = grid[i + 1][a] + (grid[i + 1][b] if a != b else 0)
                    res = max(res, score + self.getmax(grid, i + 1, a, b))
        self.cache[key] = res
        return res
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.cache = {}
        return grid[0][0] + grid[0][-1] + self.getmax(grid, 0, 0, len(grid[0]) - 1)