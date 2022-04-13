class Solution:
    def calcMin(self, dungeon, x, y, m, n):
        if (x, y) in self.cache:
            return self.cache[(x, y)]
        if (x, y) == (m - 1, n - 1):
            self.cache[(x, y)] = max(1, 1 - dungeon[m - 1][n - 1])
            return self.cache[(x, y)]
        right = float('inf')
        bottom = float('inf')
        if y < n - 1:
            right = self.calcMin(dungeon, x, y + 1, m, n)
        if x < m - 1:
            bottom = self.calcMin(dungeon, x + 1, y, m, n)
        currMin = min(right, bottom)
        self.cache[(x, y)] = max(1, currMin - dungeon[x][y])
        return self.cache[(x, y)]
    
    def calculateMinimumHP(self, dungeon):
        self.cache = {}
        return self.calcMin(dungeon, 0, 0, len(dungeon), len(dungeon[0]))