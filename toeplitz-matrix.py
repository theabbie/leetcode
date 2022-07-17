class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                k = min(i, j)
                if matrix[i][j] != matrix[i - k][j - k]:
                    return False
        return True