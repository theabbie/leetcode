from collections import *

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        q = deque([0])
        res = 0
        while q:
            curr = q.pop()
            if curr <= n:
                res = max(res, curr)
            for d in range(curr % 10, 10):
                val = 10 * curr + d
                if 0 < val <= n:
                    q.appendleft(val)
        return res