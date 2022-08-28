import bisect

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        diags = {}
        for i in range(m):
            for j in range(n):
                if i - j in diags:
                    bisect.insort(diags[i - j], mat[i][j])
                else:
                    diags[i - j] = [mat[i][j]]
        for i in range(m):
            for j in range(n):
                mat[i][j] = diags[i - j][min(i, j)]
        return mat