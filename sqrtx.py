class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        for p in range(20, -1, -1):
            pw = 1 << p
            if (sqrt + pw) * (sqrt + pw) <= x:
                sqrt += pw
        return sqrt