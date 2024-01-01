class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        vals = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    vals[j] = 0
                elif i == 0 or matrix[i - 1][j] == 0:
                    vals[j] = 1
                else:
                    vals[j] += 1
            curr = sorted(vals)
            for j in range(n):
                res = max(res, (n - j) * curr[j])
        return res