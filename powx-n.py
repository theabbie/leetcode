class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            curr = self.myPow(x, n // 2)
            return curr * curr
        else:
            curr = self.myPow(x, (n - 1) // 2)
            return x * curr * curr