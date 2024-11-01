class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vals = {}
        for i in range(n):
            for h in grid[i]:
                if h not in vals:
                    vals[h] = []
                vals[h].append(i)
        vals = list(vals.items())
        @lru_cache(maxsize = None)
        def maxval(i, mask):
            if i >= len(vals):
                return 0
            res = maxval(i + 1, mask)
            for j in vals[i][1]:
                if not mask & (1 << j):
                    res = max(res, vals[i][0] + maxval(i + 1, mask | (1 << j)))
            return res
        return maxval(0, 0)