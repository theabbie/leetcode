class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        x = y = z = n - 1
        for i in range(n - 1, -1, -1):
            while x >= i and days[x] - days[i] >= 1:
                x -= 1
            while y >= i and days[y] - days[i] >= 7:
                y -= 1
            while z >= i and days[z] - days[i] >= 30:
                z -= 1
            dp[i] = min(costs[0] + dp[x + 1], costs[1] + dp[y + 1], costs[2] + dp[z + 1])
        return dp[0]