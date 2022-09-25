class Solution:
    def verticalFlip(self, matrix, n):
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    
    def diagonalFlip(self, matrix, n):
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def equals(self, m1, m2, n):
        for i in range(n):
            for j in range(n):
                if m1[i][j] != m2[i][j]:
                    return False
        return True
        
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if self.equals(mat, target, n):
                return True
            self.verticalFlip(mat, n)
            self.diagonalFlip(mat, n)
        return False