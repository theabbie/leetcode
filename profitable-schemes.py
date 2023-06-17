M = 10 ** 9 + 7

class Solution:
    def count(self, i, rem, curr, group, profit):
        if i >= len(group):
            if curr >= 0:
                return 1
            return 0
        key = (i, rem, curr)
        if key in self.cache:
            return self.cache[key]
        res = 0
        res += self.count(i + 1, rem, curr, group, profit)
        if rem >= group[i]:
            res += self.count(i + 1, rem - group[i], curr + profit[i], group, profit)
        res %= M
        self.cache[key] = res
        return res
    
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        self.cache = {}
        seq = sorted(range(m), key = lambda i: -group[i])
        group = [group[i] for i in seq]
        profit = [profit[i] for i in seq]
        return self.count(0, n, -minProfit, group, profit)