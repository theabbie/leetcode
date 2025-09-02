class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        ctr = [0] * (n * n + 1)
        
        for row in grid:
            for num in row:
                ctr[num] += 1
        
        a = b = -1
        for i in range(1, n * n + 1):
            if ctr[i] == 2:
                a = i
            elif ctr[i] == 0:
                b = i
        
        return [a, b]