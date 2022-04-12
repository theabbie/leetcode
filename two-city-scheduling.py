from functools import cmp_to_key

class Solution:
    def compare(self, cost1, cost2):
        a, b = cost1
        c, d = cost2
        if a + d <= b + c:
            return -1
        return 1
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key = cmp_to_key(self.compare))
        cost = 0
        for i in range(n // 2):
            cost += costs[i][0]
        for i in range(n // 2, n):
            cost += costs[i][1]
        return cost