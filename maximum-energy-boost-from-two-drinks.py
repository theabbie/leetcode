class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0, 0] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            dp[i][0] = max(dp[i][0], energyDrinkA[i] + dp[i + 1][0])
            dp[i][1] = max(dp[i][1], energyDrinkB[i] + dp[i + 1][1])
            if i + 2 <= n:
                dp[i][0] = max(dp[i][0], energyDrinkA[i] + dp[i + 2][1])
                dp[i][1] = max(dp[i][1], energyDrinkB[i] + dp[i + 2][0])
        return max(dp[0])