import math

class Solution:
    def reverse(self, x: int) -> int:
        LIMIT = (1 << 31) - 1
        if x == 0:
            return x
        sign = x//abs(x)
        x = abs(x)
        op = 0
        while x > 0:
            d = x % 10
            x = x // 10
            op = 10 * op + d
            if (sign == 1 and op > LIMIT) or (sign == -1 and op > LIMIT + 1):
                return 0
        return op * sign