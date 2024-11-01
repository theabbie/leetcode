class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        x = []
        y = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        x.sort()
        y.sort()
        res = 0
        for el in x:
            res += abs(el - x[len(x) // 2])
        for el in y:
            res += abs(el - y[len(y) // 2])
        return res