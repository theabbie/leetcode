class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key = lambda p: -matrix[p[0]][p[1]])
        dp = [[1] * n for _ in range(m)]
        res = 1
        for i, j in points:
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[x][y])
                    res = max(res, dp[i][j])
        return res