class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        p = piles[:]
        for i in range(n - 2, -1, -1):
            p[i] += p[i + 1]
        p.append(0)
        dp = [[0] * 101 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for m in range(1, 101):
                curr = 0
                for j in range(i, min(i + 2 * m, n)):
                    curr += piles[j]
                    dp[i][m] = max(dp[i][m], curr + p[j + 1] - dp[j + 1][max(j - i + 1, m)])
        return dp[0][1]