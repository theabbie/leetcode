class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for s in range(amount + 1):
                if s >= c:
                    dp[s] += dp[s - c]
        return dp[amount]