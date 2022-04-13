class Solution:
    memo = {}
    
    def minCostClimbingStairsRec(self, i, cost):
        if i > len(cost) - 1:
            return 0
        if i == len(cost) - 1:
            return cost[i]
        if i not in self.memo:
            self.memo[i] = cost[i] + min(self.minCostClimbingStairsRec(i + 1, cost), self.minCostClimbingStairsRec(i + 2, cost))
        return self.memo[i]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        return min(self.minCostClimbingStairsRec(0, cost), self.minCostClimbingStairsRec(1, cost))
        