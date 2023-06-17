class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minSoFar = prices[0]
        maxDiffSoFar = 0
        for i in range(1, n):
            minSoFar = min(minSoFar, prices[i])
            maxDiffSoFar = max(maxDiffSoFar, prices[i] - minSoFar)
        return maxDiffSoFar