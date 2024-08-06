class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mnx = m + 1
        mxx = -1
        mny = n + 1
        mxy = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mnx = min(mnx, i)
                    mxx = max(mxx, i)
                    mny = min(mny, j)
                    mxy = max(mxy, j)
        return (mxx - mnx + 1) * (mxy - mny + 1)