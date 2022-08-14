class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[float('-inf')] * (n - 2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                for a in range(i - 1, i + 2):
                    for b in range(j - 1, j + 2):
                        res[i - 1][j - 1] = max(res[i - 1][j - 1], grid[a][b])
        return res