from sortedcontainers import SortedList

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        dp = [[float('-inf')] * (n + 1) for _ in range(n + 1)]
        ndp = [[float('-inf')] * (n + 1) for _ in range(n + 1)]
        maxes = [[float('-inf')] * n for _ in range(n)]
        for i in range(m - 1, -1, -1):
            vals = SortedList()
            for j in range(n):
                vals.add(board[i][j])
            for j in range(n):
                vals.remove(board[i][j])
                for k in range(j + 1, n):
                    vals.remove(board[i][k])
                    maxes[j][k] = vals[-1]
                    vals.add(board[i][k])
                vals.add(board[i][j])
            for f in range(n + 1):
                mxl = [float('-inf')] * (n + 1)
                mxr = [float('-inf')] * (n + 1)
                for j in range(n):
                    mxl[j + 1] = max(mxl[j], board[i][j] + dp[f][j])
                    mxr[j + 1] = max(mxr[j], board[i][n - j - 1] + dp[f][n - j - 1])
                for s in range(n + 1):
                    ndp[f][s] = dp[f][s]
                    if f != n and s != n and f != s:
                        ndp[f][s] = max(ndp[f][s], maxes[min(f, s)][max(f, s)])
                    if f != n and s == n:
                        ndp[f][s] = max(ndp[f][s], mxl[f], mxr[n - f - 1])
            for s in range(n + 1):
                mval = float('-inf')
                for j in range(n):
                    mval = max(mval, board[i][j] + dp[j][s])
                for f in range(n + 1):
                    if f == n and s == n:
                        ndp[f][s] = max(ndp[f][s], mval)
            dp, ndp = ndp, dp
        return dp[n][n]