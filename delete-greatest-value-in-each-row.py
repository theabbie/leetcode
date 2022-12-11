class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            grid[i].sort(reverse = True)
        res = 0
        for j in range(n):
            curr = float('-inf')
            for i in range(m):
                curr = max(curr, grid[i][j])
            res += curr
        return res