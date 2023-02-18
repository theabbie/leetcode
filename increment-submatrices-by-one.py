class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n + 1) for _ in range(n)]
        for a, b, c, d in queries:
            for i in range(a, c + 1):
                mat[i][b] += 1
                mat[i][d + 1] -= 1
        for i in range(n):
            for j in range(1, n + 1):
                mat[i][j] += mat[i][j - 1]
        for i in range(n):
            mat[i].pop()
        return mat