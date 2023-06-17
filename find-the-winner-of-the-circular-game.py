class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for x in range(2, n + 1):
            res += k
            res %= x
        return res + 1