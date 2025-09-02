class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[float('-inf'), float('-inf'), float('-inf')] for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n - 1] = [0, 0, 0]
        dp[m - 1][n] = [0, 0, 0]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                for rem in range(3):
                    if rem > 0:
                        dp[i][j][rem] = max(dp[i][j][rem], dp[i][j][rem - 1])
                        dp[i][j][rem] = max(dp[i][j][rem], dp[i + 1][j][rem - 1], dp[i][j + 1][rem - 1])
                    dp[i][j][rem] = max(dp[i][j][rem], coins[i][j] + max(dp[i + 1][j][rem], dp[i][j + 1][rem]))
        return dp[0][0][2]