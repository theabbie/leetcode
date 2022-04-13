class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = [1, -1][(dividend >= 0) ^ (divisor >= 0)]
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                temp = temp << 1
                i = i << 1
        return min(max(-2147483648, sign * res), 2147483647)