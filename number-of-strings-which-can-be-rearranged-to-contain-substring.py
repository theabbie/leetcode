from collections import defaultdict

M = 10 ** 9 + 7

class Solution:
    def stringCount(self, n: int) -> int:
        dp = [defaultdict(lambda: 0) for _ in range(n + 1)]
        dp[n][(1, 2, 1)] = 1
        for i in range(n - 1, -1, -1):
            for l in range(2):
                for e in range(3):
                    for t in range(2):
                        dp[i][(l, e, t)] += dp[i + 1][(min(l + 1, 1), e, t)] + dp[i + 1][(l, min(e + 1, 2), t)] + dp[i + 1][(l, e, min(t + 1, 1))]
                        dp[i][(l, e, t)] += 23 * dp[i + 1][(l, e, t)]
                        dp[i][(l, e, t)] %= M
        return dp[i][(0, 0, 0)]
        