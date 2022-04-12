class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        stocks = sorted(range(n), key = lambda i: 1000000 * prices[i] + i)
        print(stocks)
        if stocks[-1] > stocks[0]:
            return prices[stocks[-1]] - prices[stocks[0]] - 1
        return 0

print(Solution.maxProfit(Solution, [7,1,5,3,6,4]))