from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ctr = defaultdict(int)
        for i in range(m):
            a = 0
            b = 0
            for j in range(n):
                a = 2 * a + matrix[i][j]
                b = 2 * b + 1 - matrix[i][j]
            ctr[min(a, b)] += 1
        return max(ctr.values())