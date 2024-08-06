class Solution:
    def minChanges(self, n: int, k: int) -> int:
        res = 0
        for b in range(32):
            if k & (1 << b) and not n & (1 << b):
                return -1
            if n & (1 << b) and not k & (1 << b):
                res += 1
        return res