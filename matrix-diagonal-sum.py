class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = -mat[n//2][n//2] if n & 1 else 0
        for i in range(n):
            total += mat[i][i] + mat[i][n-i-1]
        return total