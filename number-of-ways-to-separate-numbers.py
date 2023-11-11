M = 10 ** 9 + 7

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        dp = [[0] * (n + 1) for _ in range(n)]
        lcp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                lcp[i][j] = 1 + lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 1
                if num[i] != num[j]:
                    lcp[i][j] = 0
        for i in range(n - 1, -1, -1):
            if num[i] == "0":
                continue
            for l in range(n - i, 0, -1):
                if l < n:
                    dp[i][l] += dp[i][l + 1]
                if i + l == n:
                    dp[i][l] += 1
                    continue
                if i + 2 * l > n or lcp[i][i + l] >= l or num[i + lcp[i][i + l]] < num[i + l + lcp[i][i + l]]:
                    dp[i][l] += dp[i + l][l]
                else:
                    dp[i][l] += dp[i + l][l + 1]
                dp[i][l] %= M
        return dp[0][1]