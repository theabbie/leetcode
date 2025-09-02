class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        sub = self.myPow(x, n // 2)
        res = sub * sub
        if n % 2 == 1:
            res *= x
        return res