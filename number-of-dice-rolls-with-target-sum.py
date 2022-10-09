class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for __ in range(n)]
        for i in range(1, k + 1):
            if i <= target:
                dp[0][i] = 1
        for i in range(1, n):
            for l in range(target + 1):
                for j in range(1, k + 1):
                    if j <= l:
                        dp[i][l] += dp[i - 1][l - j]
        return dp[n - 1][target] % (10 ** 9 + 7)