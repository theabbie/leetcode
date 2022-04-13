class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort()
        curr = 0
        if len(cost) == 1:
            return cost[0]
        while len(cost) > 1:
            b = cost.pop()
            a = cost.pop()
            curr += a + b
            if len(cost) > 0:
                cost.pop()
        curr += sum(cost)
        return curr