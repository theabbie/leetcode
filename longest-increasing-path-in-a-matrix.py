class Solution:
    def getNeighbours(self, i, j, m, n):
        for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
            if 0 <= x < m and 0 <= y < n:
                yield (x, y)
    
    def longestTill(self, matrix, i, j, m, n):
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        mlen = 1
        for x, y in self.getNeighbours(i, j, m, n):
            if matrix[x][y] > matrix[i][j]:
                curr = 1 + self.longestTill(matrix, x, y, m, n)
                mlen = max(mlen, curr)
        self.cache[(i, j)] = mlen
        return mlen
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        mlen = 1
        self.cache = {}
        for i in range(m):
            for j in range(n):
                if (i, j) not in self.cache:
                    curr = self.longestTill(matrix, i, j, m, n)
                    mlen = max(mlen, curr)
        return mlen