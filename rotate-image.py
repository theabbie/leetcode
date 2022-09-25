class Solution:
    def verticalFlip(self, matrix, n):
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    
    def diagonalFlip(self, matrix, n):
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        self.verticalFlip(matrix, n)
        self.diagonalFlip(matrix, n)