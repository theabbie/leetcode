class Solution:
    def dfs(self, node, parent, vis, tin, low, mark, graph):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0
        for it in graph[node]:
            if it == parent:
                continue
            if not vis[it]:
                self.dfs(it, node, vis, tin, low, mark, graph)
                low[node] = min(low[node], low[it])
                if low[it] >= tin[node] and parent != -1:
                    mark[node] = 1
                child += 1
            else:
                low[node] = min(low[node], tin[it])
        if child > 1 and parent == -1:
            mark[node] = 1
    
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        graph = [[] for _ in range(m * n)]
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                ones += 1
                for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        graph[n * i + j].append(n * x + y)
        if ones == 1:
            return 1
        self.timer = 0
        vis = [0] * (m * n)
        tin = [0] * (m * n)
        low = [0] * (m * n)
        mark = [0] * (m * n)
        comp = 0
        for i in range(m * n):
            if not vis[i] and grid[i // n][i % n] == 1:
                comp += 1
                self.dfs(i, -1, vis, tin, low, mark, graph)
        if comp == 0 or comp > 1:
            return 0
        for i in range(m * n):
            if mark[i] == 1:
                return 1
        return 2