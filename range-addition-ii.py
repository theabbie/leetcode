class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rowctr = [0 for i in range(m)]
        colctr = [0 for i in range(n)]
        for a, b in ops:
            for i in range(a):
                rowctr[i] += 1
            for i in range(b):
                colctr[i] += 1
        return rowctr.count(rowctr[0]) * colctr.count(colctr[0])