import math

class Solution:
    def minOperations(self, k: int) -> int:
        res = k - 1
        p = int(math.sqrt(k))
        for x in range(p - 10, p + 10):
            if not 0 <= x <= k:
                continue
            val = 1 + x
            rem = math.ceil(k / val)
            res = min(res, x + rem - 1)
        return res