from collections import *

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        q = deque([(n, 0)])
        res = 0
        for i in range(n - 1, -1, -1):
            while q and q[-1][0] > 2 * i + 2:
                q.pop()
            curr = prices[i] + q[-1][1]
            while q and curr < q[0][1]:
                q.popleft()
            q.appendleft((i, curr))
            res = curr
        return res