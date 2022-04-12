class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = [0]
        bottom = [0]
        for el in grid[0]:
            top.append(top[-1] + el)
        for el in grid[1]:
            bottom.append(bottom[-1] + el)
        opponent = float('inf')
        mindex = None
        for i in range(n):
            curropp = max(top[-1] - top[i + 1], bottom[i])
            if curropp <= opponent:
                opponent = curropp
                mindex = i
        return max(top[-1] - top[mindex + 1], bottom[mindex])