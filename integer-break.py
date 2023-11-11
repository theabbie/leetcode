class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n and n % 3 != 0:
            n -= 2
            res *= 2
        res *= pow(3, n // 3)
        return res