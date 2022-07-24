class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MAX = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    p = 0
                    if j - i >= 0:
                        p = dp[i - 1][j - i]
                    v = (dp[i - 1][j] + MAX - p) % MAX
                    dp[i][j] = (dp[i][j - 1] + v) % MAX
        p = 0
        if k > 0:
            p = dp[n][k - 1]
        return (dp[n][k] + MAX - p) % MAX