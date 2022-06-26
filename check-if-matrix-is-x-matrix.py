class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid[0])
        for i in range(n):
            for j in range(n):
                if i - j == 0 or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True