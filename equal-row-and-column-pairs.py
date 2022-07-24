from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        colctr = defaultdict(int)
        rowctr = defaultdict(int)
        for i in range(n):
            rowctr[tuple(grid[i])] += 1
            colctr[tuple([grid[k][i] for k in range(n)])] += 1
        res = 0
        for row in rowctr:
            res += rowctr[row] * colctr[row]
        return res