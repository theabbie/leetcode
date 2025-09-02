class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        portals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                c = matrix[i][j]
                if 'A' <= c <= 'Z':
                    portals[c].append((i, j))
        dist = [[float('inf')] * n for _ in range(m)]
        dq = deque([(0, 0)])
        dist[0][0] = 0
        while dq:
            x, y = dq.popleft()
            d = dist[x][y]
            if (x, y) == (m-1, n-1):
                return d
            c = matrix[x][y]
            if 'A' <= c <= 'Z' and portals[c]:
                for nx, ny in portals[c]:
                    if d < dist[nx][ny]:
                        dist[nx][ny] = d
                        dq.appendleft((nx, ny))
                portals[c] = []
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    nd = d + 1
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        dq.append((nx, ny))
        return -1