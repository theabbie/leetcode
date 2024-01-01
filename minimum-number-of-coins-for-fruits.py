class Solution:
    def mincoins(self, prices, i, n, right):
        if i >= n:
            return 0
        key = (i, right)
        if key in self.cache:
            return self.cache[key]
        res = float('inf')
        if i <= right:
            res = min(res, self.mincoins(prices, i + 1, n, right))
        res = min(res, prices[i] + self.mincoins(prices, i + 1, n, max(right, min(2 * i + 1, n))))
        self.cache[key] = res
        return res
    
    def minimumCoins(self, prices: List[int]) -> int:
        self.cache = {}
        return self.mincoins(prices, 0, len(prices), -1)