class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minpastvalue = float('inf')
        for price in prices:
            res = max(res, price - minpastvalue)
            minpastvalue = min(minpastvalue, price)
        return res