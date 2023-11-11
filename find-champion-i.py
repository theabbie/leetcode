class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            curr = sum(grid[x][i] for x in range(n))
            if curr == 0:
                return i
        return -1