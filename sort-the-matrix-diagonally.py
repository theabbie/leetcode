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

# import bisect

# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#         m = len(mat)
#         n = len(mat[0])
#         vals = [[] for i in range(m + n - 1)]
#         curr = 0
#         for i in range(m):
#             x, y = i, 0
#             while x < m and y < n:
#                 bisect.insort(vals[curr], mat[x][y])
#                 x += 1
#                 y += 1
#             curr += 1
#         for i in range(1, n):
#             x, y = 0, i
#             while x < m and y < n:
#                 bisect.insort(vals[curr], mat[x][y])
#                 x += 1
#                 y += 1
#             curr += 1
#         curr = 0
#         for i in range(m):
#             x, y = i, 0
#             while x < m and y < n:
#                 mat[x][y] = vals[curr][y]
#                 x += 1
#                 y += 1
#             curr += 1
#         for i in range(1, n):
#             x, y = 0, i
#             while x < m and y < n:
#                 mat[x][y] = vals[curr][x]
#                 x += 1
#                 y += 1
#             curr += 1
#         return mat