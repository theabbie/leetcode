class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ps = [(i, j) for i in range(m) for j in range(n)]
        ps.sort(key = lambda p: -mat[p[0]][p[1]])
        i = 0
        rowmax = [0] * m
        colmax = [0] * n
        dp = [[0] * n for _ in range(m)]
        res = 0
        for j in range(m * n):
            while i < j and mat[ps[i][0]][ps[i][1]] > mat[ps[j][0]][ps[j][1]]:
                rowmax[ps[i][0]] = max(rowmax[ps[i][0]], dp[ps[i][0]][ps[i][1]])
                colmax[ps[i][1]] = max(colmax[ps[i][1]], dp[ps[i][0]][ps[i][1]])
                i += 1
            dp[ps[j][0]][ps[j][1]] = 1 + max(rowmax[ps[j][0]], colmax[ps[j][1]])
            res = max(res, dp[ps[j][0]][ps[j][1]])
        return res