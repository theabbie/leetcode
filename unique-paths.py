class Solution:
    memo = {}
    
    def uniquePathsRec(self, m, n, i, j):
        if i == m - 1 or j == n - 1:
            return 1
        if (i, j) not in self.memo:
            self.memo[(i, j)] = self.uniquePathsRec(m, n, i + 1, j) + self.uniquePathsRec(m, n, i, j + 1)
        return self.memo[(i , j)]
    
    def uniquePaths(self, m: int, n: int, i = 0, j = 0) -> int:
        self.memo = {}
        return self.uniquePathsRec(m, n, 0, 0)