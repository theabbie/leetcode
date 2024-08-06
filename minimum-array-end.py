class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        inc = n - 1
        p = 0
        for b in range(62):
            if not x & (1 << b):
                if inc & (1 << p):
                    res += 1 << b
                p += 1
        return res