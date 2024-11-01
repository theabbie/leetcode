class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        if coins[0] > 1:
            return 1
        p = 0
        for i in range(len(coins)):
            p += coins[i]
            if i == len(coins) - 1 or p + 1 < coins[i + 1]:
                return p + 1