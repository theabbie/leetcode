class Solution:
    def getNeighbours(self, i, j, m, n):
        for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
            if 0 <= x < m and 0 <= y < n:
                yield (x, y)
    
    def numInc(self, matrix, i, j, m, n):
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        res = 1
        for x, y in self.getNeighbours(i, j, m, n):
            if matrix[x][y] > matrix[i][j]:
                curr = self.numInc(matrix, x, y, m, n)
                res += curr
        self.cache[(i, j)] = res
        return res
    
    def countPaths(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        self.cache = {}
        res = 0
        for i in range(m):
            for j in range(n):
                res += self.numInc(matrix, i, j, m, n)
        return res % (10 ** 9 + 7)