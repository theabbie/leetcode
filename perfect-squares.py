from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(n, 0)])
        v = {n}
        while len(q) > 0:
            curr, d = q.pop()
            if curr == 0:
                return d
            i = 0
            while i * i <= curr:
                j = curr - i * i
                if j not in v:
                    v.add(j)
                    q.appendleft((j, d + 1))
                i += 1