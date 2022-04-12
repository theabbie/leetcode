class Solution:
    def getTrees(self, beg, end):
        if beg > end:
            return 1
        if (beg, end) in self.cache:
            return self.cache[(beg, end)]
        ways = 0
        for i in range(beg, end + 1):
            ways += self.getTrees(beg, i - 1) * self.getTrees(i + 1, end)
        self.cache[(beg, end)] = ways
        return ways
    
    def numTrees(self, n: int) -> int:
        self.cache = {}
        return self.getTrees(1, n)