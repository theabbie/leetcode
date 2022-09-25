class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for el in nums:
            for b in range(32):
                if abs(el) & (1 << b):
                    bits[b] += 1
        res = 0
        for b in range(32):
            if bits[b] % 3 == 1:
                res |= 1 << b
        a = 0
        b = 0
        for el in nums:
            if el == res:
                a += 1
            if -el == res:
                b += 1
        if a == 1:
            return res
        return -res