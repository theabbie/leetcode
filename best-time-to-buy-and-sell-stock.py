# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         valIndex = {}
#         maxProfit = 0
#         for i, price in enumerate(prices):
#             if price not in valIndex:
#                 valIndex[price] = [i, i]
#             else:
#                 valIndex[price][1] = i
#         newprices = sorted(valIndex.keys())
#         n = len(newprices)
#         for j in range(n - 1, -1, -1):
#             end = newprices[j]
#             if end - newprices[0] <= maxProfit:
#                 break
#             for i in range(j):
#                 curr = end - newprices[i]
#                 if curr <= maxProfit:
#                     break
#                 if valIndex[end][1] > valIndex[newprices[i]][0]:
#                     maxProfit = max(maxProfit, curr) 
#         return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minSoFar = prices[0]
        maxDiffSoFar = 0
        for i in range(1, n):
            minSoFar = min(minSoFar, prices[i])
            maxDiffSoFar = max(maxDiffSoFar, prices[i] - minSoFar)
        return maxDiffSoFar