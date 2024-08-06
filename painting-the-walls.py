class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        ndp = dp[:]
        for i in range(n - 1, -1, -1):
            for used in range(n + 1):
                ndp[used] = min(dp[used], cost[i] + dp[min(used + time[i] + 1, n)])
            dp, ndp = ndp, dp
        return dp[0]