class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n % 3 != 0:
            res *= 2
            n -= 2
        res *= pow(3, n // 3)
        return res