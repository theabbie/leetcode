class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        res = 0
        while True:
            coins.sort()
            found = 0
            if coins[0] > 1:
                found = 1
            else:
                p = 0
                for i in range(len(coins)):
                    p += coins[i]
                    if i == len(coins) - 1 or p + 1 < coins[i + 1]:
                        found = p + 1
                        break
            if found > target:
                break
            coins.append(found)
            res += 1
        return res