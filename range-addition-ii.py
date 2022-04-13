import bisect

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rowctr = [0 for i in range(m)]
        colctr = [0 for i in range(n)]
        for a, b in ops:
            for i in range(a):
                rowctr[m - i - 1] += 1
            for i in range(b):
                colctr[n - i - 1] += 1
        return (m - bisect.bisect_left(rowctr, rowctr[-1])) * (n - bisect.bisect_left(colctr, colctr[-1]))