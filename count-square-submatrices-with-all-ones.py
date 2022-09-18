class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        sums = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sums[i][j] = matrix[i - 1][j - 1] + sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1]
        getsum = lambda r1, c1, r2, c2: sums[r2 + 1][c2 + 1] - sums[r2 + 1][c1] - sums[r1][c2 + 1] + sums[r1][c1]
        res = 0
        for i in range(m):
            for j in range(n):
                for l in range(min(m - i, n - j)):
                    if getsum(i, j, i + l, j + l) == (l + 1) * (l + 1):
                        res += 1
                    else:
                        break
        return res