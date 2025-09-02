class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c = num2.bit_count()
        res = 0
        for b in range(32, -1, -1):
            if c and (b + 1 == c or num1 & (1 << b)):
                res += (1 << b)
                c -= 1
        return res