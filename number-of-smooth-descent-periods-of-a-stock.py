class Solution:
    def deslen(self, prices, i, n):
        if i in self.cache:
            return self.cache[i]
        if i == n - 1 or prices[i] - prices[i + 1] != 1:
            self.cache[i] = 1
            return 1
        val = 1 + self.deslen(prices, i + 1, n)
        self.cache[i] = val
        return val
    
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        self.cache = {}
        ctr = 0
        for i in range(n):
            ctr += self.deslen(prices, i, n)
        return ctr