class Solution:
    def profit(self, prices, i, n, sign, fee):
        if i >= n:
            return 0
        key = (i, sign)
        if key in self.cache:
            return self.cache[key]
        a = sign * prices[i] + self.profit(prices, i + 1, n, -sign, fee)
        b = self.profit(prices, i + 1, n, sign, fee)
        if sign == -1:
            a -= fee
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        self.cache = {}
        return self.profit(prices, 0, n, -1, fee)