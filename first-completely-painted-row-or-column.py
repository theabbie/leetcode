class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rowctr = [0] * m
        colctr = [0] * n
        l = len(arr)
        pos = {}
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)
        for i in range(l):
            x, y = pos[arr[i]]
            rowctr[x] += 1
            colctr[y] += 1
            if rowctr[x] == n:
                return i
            if colctr[y] == m:
                return i