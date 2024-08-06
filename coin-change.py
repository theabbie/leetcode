class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return 1
        coins = [c for c in coins if c < amount]
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i + c <= amount:
                    dp[i + c] = min(dp[i + c], 1 + dp[i])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]