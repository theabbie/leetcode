import bisect

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        vals = [[] for i in range(m + n - 1)]
        curr = 0
        for i in range(m):
            x, y = i, 0
            while x < m and y < n:
                bisect.insort(vals[curr], mat[x][y])
                x += 1
                y += 1
            curr += 1
        for i in range(1, n):
            x, y = 0, i
            while x < m and y < n:
                bisect.insort(vals[curr], mat[x][y])
                x += 1
                y += 1
            curr += 1
        curr = 0
        for i in range(m):
            x, y = i, 0
            while x < m and y < n:
                mat[x][y] = vals[curr][y]
                x += 1
                y += 1
            curr += 1
        for i in range(1, n):
            x, y = 0, i
            while x < m and y < n:
                mat[x][y] = vals[curr][x]
                x += 1
                y += 1
            curr += 1
        return mat