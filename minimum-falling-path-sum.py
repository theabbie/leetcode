class Solution:
    def minSum(self, matrix, i, j, m, n):
        if i == m - 1:
            return matrix[i][j]
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        minPath = float('inf')
        for col in [j - 1, j, j + 1]:
            if 0 <= col < n:
                minPath = min(minPath, matrix[i][j] + self.minSum(matrix, i + 1, col, m, n))
        self.cache[(i, j)] = minPath
        return minPath
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        self.cache = {}
        minPath = float('inf')
        for i in range(n):
            minPath = min(minPath, self.minSum(matrix, 0, i, m, n))
        return minPath