class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and sum(grid[0]) == 0:
            return [0]
        pos = {}
        for i in range(m):
            for mask in range(1 << n):
                valid = True
                for j in range(n):
                    if mask & (1 << j) and grid[i][j] + 1 > 1:
                        valid = False
                        break
                if valid and mask in pos:
                    return [pos[mask], i]
            curr = 0
            for j in range(n):
                if grid[i][j] == 1:
                    curr |= 1 << j
            pos[curr] = i
        return []