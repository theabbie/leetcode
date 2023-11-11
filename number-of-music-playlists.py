M = 10 ** 9 + 7

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                if j > i:
                    continue
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1)
                if j > k:
                    dp[i][j] += dp[i - 1][j] * (j - k)
                dp[i][j] %= M
        return dp[goal][n]