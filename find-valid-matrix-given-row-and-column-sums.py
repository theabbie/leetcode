class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = [[0] * n for _ in range(m)]
        for _ in range(m * n):
            x = y = 0
            rval = cval = float('inf')
            for i in range(m):
                if rowSum[i] > 0 and rowSum[i] < rval:
                    rval = rowSum[i]
                    x = i
            for j in range(n):
                if colSum[j] > 0 and colSum[j] < cval:
                    cval = colSum[j]
                    y = j
            val = min(rval, cval)
            if val == float('inf'):
                break
            res[x][y] = val
            rowSum[x] -= val
            colSum[y] -= val
        return res