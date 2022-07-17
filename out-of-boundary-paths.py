class Solution:
    def find(self, i, j, m, n, rem):
        if rem < 0:
            return 0
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        key = (i, j, rem)
        if key in self.cache:
            return self.cache[key]
        ctr = 0
        for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
            ctr += self.find(x, y, m, n, rem - 1)
        self.cache[key] = ctr
        return ctr
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.cache = {}
        return self.find(startRow, startColumn, m, n, maxMove) % (10 ** 9 + 7)