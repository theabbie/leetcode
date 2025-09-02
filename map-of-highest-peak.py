class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        dist = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for nx, ny in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        return dist