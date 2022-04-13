class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        op = [[-1 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                op[j][i] = matrix[i][j]
        return op