class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = [[[float('inf')] * 4 for _ in range(4)] for _ in range(n // 2 + 1)]
        for pl in range(-1, 3):
            for pr in range(-1, 3):
                dp[n // 2][pl][pr] = 0
        for i in range(n // 2 - 1, -1, -1):
            for pl in range(-1, 3):
                for pr in range(-1, 3):
                    for f in range(3):
                        for s in range(3):
                            if f != s and f != pl and s != pr:
                                dp[i][pl][pr] = min(dp[i][pl][pr], cost[i][f] + cost[n - i - 1][s] + dp[i + 1][f][s])
        return dp[0][-1][-1]