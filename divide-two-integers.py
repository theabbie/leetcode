class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = [1, -1][(dividend >= 0) ^ (divisor >= 0)]
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        beg = 0
        end = dividend
        while beg <= end:
            mid = (beg + end) // 2
            if divisor * mid <= dividend:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return min(max(-2147483648, sign * res), 2147483647)