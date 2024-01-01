class Solution:
    def cost(self, cost, i, j, m, n, took, used):
        if i >= m:
            if used + 1 != 1 << n:
                return float('inf')
            return 0
        key = (i, j, took, used)
        if key in self.cache:
            return self.cache[key]
        res = float('inf')
        newi = i
        newj = j + 1
        if newj >= n:
            newi += 1
            newj = 0
        res = min(res, cost[i][j] + self.cost(cost, newi, newj, m, n, bool(newj != 0), used | (1 << j)))
        if j != n - 1 or took:
            res = min(res, self.cost(cost, newi, newj, m, n, bool(took and newj != 0), used))
        self.cache[key] = res
        return res
    
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m = len(cost)
        n = len(cost[0])
        self.cache = {}
        return self.cost(cost, 0, 0, m, n, False, 0)