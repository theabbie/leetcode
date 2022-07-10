class Solution:
    def mcost(self, cost, i, n):
        if i >= n:
            return 0
        if i in self.cache:
            return self.cache[i]
        res = cost[i] + min(self.mcost(cost, i + 1, n), self.mcost(cost, i + 2, n))
        self.cache[i] = res
        return res
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cache = {}
        n = len(cost)
        return min(self.mcost(cost, 0, n), self.mcost(cost, 1, n))