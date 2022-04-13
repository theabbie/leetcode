class Solution:
    def minPath(self, triangle, i, j, n):
        if i == n - 1:
            return triangle[i][j]
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        currmin = min(self.minPath(triangle, i + 1, j, n), self.minPath(triangle, i + 1, j + 1, n))
        self.cache[(i, j)] = triangle[i][j] + currmin
        return self.cache[(i, j)]
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.cache = {}
        return self.minPath(triangle, 0, 0, len(triangle))