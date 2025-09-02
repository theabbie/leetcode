M = 10 ** 9 + 7

class Solution:
    def numOfWays(self, n: int) -> int:
        vals = []
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if a != b and b != c:
                        vals.append((a, b, c))
        dp = defaultdict(int)
        for v in vals:
            dp[v] = 1
        ndp = defaultdict(int)
        for i in range(1, n):
            for curr in vals:
                ndp[curr] = 0
                for prev in vals:
                    if curr[0] != prev[0] and curr[1] != prev[1] and curr[2] != prev[2]:
                        ndp[curr] += dp[prev]
                        ndp[curr] %= M
            dp, ndp = ndp, dp
        return sum(dp.values()) % M