class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        cmax = [float('-inf')] * n
        for i in range(m):
            for j in range(n):
                cmax[j] = max(cmax[j], matrix[i][j])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = cmax[j]
        return matrix