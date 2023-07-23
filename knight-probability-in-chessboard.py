class Solution:
    def prob(self, i, j, n, rem):
        if not 0 <= i < n or not 0 <= j < n:
            return 0
        if rem == 0:
            return 1
        key = (i, j, rem)
        if key in self.cache:
            return self.cache[key]
        p = 0
        for dx in [-2, -1, 1, 2]:
            for dy in [-2, -1, 1, 2]:
                if abs(dx) == abs(dy):
                    continue
                p += self.prob(i + dx, j + dy, n, rem - 1)
        p /= 8
        self.cache[key] = p
        return p
    
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.cache = {}
        return self.prob(row, column, n, k)