class Solution:
    def DFS(self, i, j, m, n, heights, visited):
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= i + di < m and 0 <= j + dj < n:
                if (i + di, j + dj) not in visited and heights[i + di][j + dj] <= heights[i][j]:
                    visited.add((i + di, j + dj))
                    self.DFS(i + di, j + dj, m, n, heights, visited)
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set([(i, 0) for i in range(m)] + [(0, i) for i in range(n)])
        atlantic = set([(i, n - 1) for i in range(m)] + [(m - 1, i) for i in range(n)])
        op = []
        for i in range(m):
            for j in range(n):
                visited = {(i, j)}
                self.DFS(i, j, m, n, heights, visited)
                if len(set.intersection(visited, pacific)) > 0 and len(set.intersection(visited, atlantic)) > 0:
                    op.append([i, j])
        return op