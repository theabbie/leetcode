import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = math.floor((math.sqrt(1 + 8 * n) - 1) / 2)
        return k