class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def ctr(val, a, b):
            res = 0
            while a <= val:
                res += min(val + 1, b) - a
                a *= 10
                b *= 10
            return res
        k -= 1
        res = 1
        while k:
            c = ctr(n, res, res + 1)
            if c <= k:
                res += 1
                k -= c
            else:
                res *= 10
                k -= 1
        return res