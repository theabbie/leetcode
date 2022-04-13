class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        cache = {}
        for i in range(n):
            for j in range(n):
                cache[(i, j)] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                matrix[j][n - i - 1] = cache[(i, j)]