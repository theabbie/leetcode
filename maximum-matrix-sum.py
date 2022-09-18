class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = 0
        maxneg = float('-inf')
        minpos = float('inf')
        ctr = 0
        for i in range(n):
            for j in range(n):
                res += abs(matrix[i][j])
                if matrix[i][j] <= 0:
                    ctr += 1
                    maxneg = max(maxneg, matrix[i][j])
                else:
                    minpos = min(minpos, matrix[i][j])
        if ctr % 2 == 0:
            maxneg = 0
        return max(res + 2 * maxneg, res - 2 * minpos)