class Solution:
    def profit(self, prices, i, n, sign):
        if i >= n:
            return 0
        key = (i, sign)
        if key in self.cache:
            return self.cache[key]
        a = sign * prices[i] + self.profit(prices, i + 1, n, -sign)
        b = self.profit(prices, i + 1, n, sign)
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        self.cache = {}
        return self.profit(prices, 0, n, -1)