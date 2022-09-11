class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxStarting = [float('-inf')] * n
        mval = 0
        for i in range(n - 1, -1, -1):
            maxStarting[i] = max(mval - prices[i], 0)
            mval = max(mval, prices[i])
        res = 0
        mval = float('-inf')
        minstock = float('inf')
        for i in range(n):
            minstock = min(minstock, prices[i])
            mval = max(mval, prices[i] - minstock, 0)
            res = max(res, mval + maxStarting[i])
        return res