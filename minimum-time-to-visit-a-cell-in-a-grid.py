import heapq
import math

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        time = [[float('inf')] * n for _ in range(m)]
        time[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            d, i, j = heapq.heappop(heap)
            if (i, j) == (m - 1, n - 1):
                return d
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:
                    ntime = d + 1
                    if d + 1 < grid[x][y]:
                        diff = grid[x][y] - d - 1
                        ntime = d + 1 + 2 * math.ceil(diff / 2)
                    if ntime < time[x][y]:
                        time[x][y] = ntime
                        heapq.heappush(heap, (ntime, x, y))
        return -1