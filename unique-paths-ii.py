class Solution:
    memo = {}
    
    def uniquePathsRec(self, m, n, i, j, obstacleGrid):
        if i == m - 1 and j == n - 1:
            if obstacleGrid[i][j] != 1:
                return 1
            return 0
        if obstacleGrid[i][j] == 1:
            return 0
        if (i, j) not in self.memo:
            self.memo[(i, j)] = 0
            if i + 1 < m:
                self.memo[(i, j)] += self.uniquePathsRec(m, n, i + 1, j, obstacleGrid)
            if j + 1 < n:
                self.memo[(i, j)] += self.uniquePathsRec(m, n, i, j + 1, obstacleGrid)
        return self.memo[(i , j)]  
            
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.memo = {}
        return self.uniquePathsRec(len(obstacleGrid), len(obstacleGrid[0]), 0, 0, obstacleGrid)