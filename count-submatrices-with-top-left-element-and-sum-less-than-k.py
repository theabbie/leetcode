class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        sums = [0] * n
        for i in range(m):
            for j in range(n):
                sums[j] += grid[i][j]
            curr = 0
            for j in range(n):
                curr += sums[j]
                if curr <= k:
                    res += 1
        return res