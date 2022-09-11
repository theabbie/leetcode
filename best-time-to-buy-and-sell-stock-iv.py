class Solution:
    def profit(self, prices, i, n, sign, rem):
        if i >= n or rem == 0:
            return 0
        key = (i, sign, rem)
        if key in self.cache:
            return self.cache[key]
        a = sign * prices[i] + self.profit(prices, i + 1, n, -sign, rem - 1)
        b = self.profit(prices, i + 1, n, sign, rem)
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        self.cache = {}
        return self.profit(prices, 0, n, -1, 2 * k)