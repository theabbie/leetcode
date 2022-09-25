class Solution:
    def mySqrt(self, x: int) -> int:
        beg = 0
        end = x
        res = 0
        while beg <= end:
            mid = (beg + end) // 2
            if mid * mid <= x:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res