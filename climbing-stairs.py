class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n == 1:
            return a
        for _ in range(n - 2):
            a, b = b, a + b
        return b