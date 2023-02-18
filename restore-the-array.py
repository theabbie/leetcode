class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        M = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            v = 0
            for j in range(i, n):
                v = 10 * v + int(s[j])
                if 1 <= v <= k:
                    dp[i] += dp[j + 1]
                    dp[i] %= M
                else:
                    break
        return dp[0]