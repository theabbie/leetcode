class Solution:
    def mySqrt(self, x: int) -> int:
        beg = 0
        end = x
        while beg <= end:
            mid = (beg + end) // 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid > x:
                end = mid
            else:
                beg = mid + 1