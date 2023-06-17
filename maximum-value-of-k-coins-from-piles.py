class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for rem in range(1, k + 1):
                dp[i][rem] = dp[i + 1][rem]
                val = 0
                for j in range(min(rem, len(piles[i]))):
                    val += piles[i][j]
                    dp[i][rem] = max(dp[i][rem], val + dp[i + 1][rem - j - 1])
        return dp[0][k]