class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        res = [float('inf')] * n
        
        for i in range(n):
            res[i] = min(res[i], cost[i])
            if i > 0:
                res[i] = min(res[i], res[i - 1])
        
        return res