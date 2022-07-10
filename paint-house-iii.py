class Solution:
    def minpaint(self, houses, i, cost, rem, m, n, prev):
        if rem < 0:
            return float('inf')
        if i == m:
            if rem == 0:
                return 0
            return float('inf')
        if (i, rem, prev) in self.cache:
            return self.cache[(i, rem, prev)]
        if houses[i] != 0:
            newrem = rem
            if houses[i] != prev:
                newrem -= 1
            return self.minpaint(houses, i + 1, cost, newrem, m, n, houses[i])
        mincost = float('inf')
        for j in range(1, n + 1):
            newrem = rem
            if j != prev:
                newrem -= 1
            curr = cost[i][j - 1] + self.minpaint(houses, i + 1, cost, newrem, m, n, j)
            mincost = min(mincost, curr)
        self.cache[(i, rem, prev)] = mincost
        return mincost
    
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.cache = {}
        res = self.minpaint(houses, 0, cost, target, m, n, -1)
        if res == float('inf'):
            return -1
        return res