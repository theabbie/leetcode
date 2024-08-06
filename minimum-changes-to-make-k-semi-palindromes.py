class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[float('inf')] * (n + 1) for _ in range(n)]
        diff = [[0] * n for _ in range(n)]
        curr = [[float('inf') if l > 1 else 0 for l in range(n + 1)] for _ in range(n)]
        for d in range(1, n + 1):
            for i in range(n - d + 1):
                for j in range(n - d + 1):
                    diff[i][j] += int(s[i + d - 1] != s[j + d - 1])
            l = 2 * d
            while l <= n:
                for i in range(n - l + d - 1, -1, -1):
                    curr[i][d] = 0
                    curr[i][l] = curr[i + d][l - 2 * d] + diff[i][i + l - d]
                    cost[i][l] = min(cost[i][l], curr[i][l])
                l += d
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for l in range(1, n + 1):
            for rem in range(1, k + 1):
                for m in range(2, l + 1):
                    dp[l][rem] = min(dp[l][rem], cost[l - m][m] + dp[l - m][rem - 1])
        return dp[n][k]