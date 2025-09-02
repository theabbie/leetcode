import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        v = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    v[i][j] = True
        res = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and not v[x][y]:
                    v[x][y] = True
                    if heightMap[x][y] < h:
                        res += h - heightMap[x][y]
                    heightMap[x][y] = max(heightMap[x][y], h)
                    heapq.heappush(heap, (heightMap[x][y], x, y))
        return res