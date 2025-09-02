import heapq
import bisect

class Solution:
    def maxPoints(self, grid, queries):
        m = len(grid)
        n = len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        v = {(0, 0)}
        order = []
        while len(heap) > 0:
            curr, i, j = heapq.heappop(heap)
            order.append(curr)
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in v:
                    v.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))
        myet = float('-inf')
        for i in range(len(order)):
            myet = max(myet, order[i])
            order[i] = myet
        res = []
        for q in queries:
            res.append(bisect.bisect_left(order, q))
        return res