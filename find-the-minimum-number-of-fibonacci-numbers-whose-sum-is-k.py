import bisect

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 1]
        for _ in range(45):
            fibs.append(fibs[-2] + fibs[-1])
        res = 0
        while k:
            pos = bisect.bisect_left(fibs, k)
            if fibs[pos] > k:
                pos -= 1
            k -= fibs[pos]
            res += 1
        return res