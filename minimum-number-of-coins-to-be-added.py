from sortedcontainers import SortedList

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins = SortedList(coins)
        res = 0
        if coins[0] != 1:
            res += 1
            coins.add(1)
        coins.add(float('inf'))
        p = 0
        i = 0
        while i < len(coins) - 1:
            p += coins[i]
            if p + 1 <= target and p + 1 < coins[i + 1]:
                coins.add(p + 1)
                res += 1
            i += 1
        return res