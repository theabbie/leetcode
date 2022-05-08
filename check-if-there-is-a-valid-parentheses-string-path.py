from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def hasPath(self, i, j, m, n, ctr):
        pmap = { '(': 1, ')': -1 }
        if ctr >= 0 and 0 <= i < m and 0 <= j < n:
            curr = self.grid[i][j]
            ctr += pmap[curr]
            if (i, j) == (m - 1, n - 1):
                return ctr == 0
            if self.hasPath(i + 1, j, m, n, ctr) or self.hasPath(i, j + 1, m, n, ctr):
                return True
        return False
    
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        self.grid = grid
        return self.hasPath(0, 0, m, n, 0)