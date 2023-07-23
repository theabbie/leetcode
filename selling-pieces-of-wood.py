class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p
        for h in range(m + 1):
            for w in range(n + 1):
                for hh in range(1, h):
                    dp[h][w] = max(dp[h][w], dp[hh][w] + dp[h - hh][w])
                for ww in range(1, w):
                    dp[h][w] = max(dp[h][w], dp[h][ww] + dp[h][w - ww])
        return dp[m][n]