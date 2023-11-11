class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = -1
        p = pow(2, 32)
        for i in range(32, -1, -1):
            if (sqrt + p) * (sqrt + p) <= x:
                sqrt += p
            p //= 2
        return sqrt