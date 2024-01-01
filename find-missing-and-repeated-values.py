class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        rem = set(range(1, n * n + 1))
        res = [-1, -1]
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    res[0] = grid[i][j]
                seen.add(grid[i][j])
                if grid[i][j] in rem:
                    rem.remove(grid[i][j])
        res[1] = min(rem)
        return res