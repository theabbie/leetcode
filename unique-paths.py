class Solution:
    def uniquePathsRec(self, m, n, i, j):
        if i == m - 1 or j == n - 1:
            return 1
        if (i, j) in self.cache:
            return self.cache[(i , j)]
        res = self.uniquePathsRec(m, n, i + 1, j) + self.uniquePathsRec(m, n, i, j + 1)
        self.cache[(i, j)] = res
        return res
    
    def uniquePaths(self, m: int, n: int, i = 0, j = 0) -> int:
        self.cache = {}
        return self.uniquePathsRec(m, n, 0, 0)