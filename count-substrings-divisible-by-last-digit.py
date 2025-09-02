class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * 10 for _ in range(10)]
        res = 0
        for i in range(n):
            ndp = [[0] * 10 for _ in range(10)]
            curr = int(s[i])
            for m in range(1, 10):
                for r in range(10):
                    if dp[m][r]:
                        ndp[m][(10 * r + curr) % m] += dp[m][r]
            for m in range(1, 10):
                ndp[m][curr % m] += 1
            if curr:
                res += ndp[curr][0]
            dp = ndp
        return res