from collections import deque

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        if n == 1:
            return 0
        price.sort()
        def possible(price, n, gap):
            i = 0
            rem = k - 1
            for j in range(n):
                if price[j] - price[i] >= gap:
                    rem -= 1
                    i = j
            return rem <= 0
        beg = 0
        end = price[-1] - price[0]
        res = 0
        while beg <= end:
            mid = (beg + end) // 2
            if possible(price, n, mid):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res