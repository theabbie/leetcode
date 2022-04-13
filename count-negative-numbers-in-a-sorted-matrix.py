class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ctr = 0
        for i in range(m):
            beg = 0
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                if beg == end:
                    if grid[i][beg] < 0:
                        ctr += (n - beg)
                    break
                elif grid[i][mid] >= 0:
                    beg = mid + 1
                else:
                    end = mid
        return ctr