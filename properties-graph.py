class Solution:
    def numberOfComponents(self, p: List[List[int]], k: int) -> int:
        n = len(p)
        g = [[] for _ in range(n)]
        for i in range(n):
            s = set(p[i])
            for j in range(i + 1, n):
                if len(s.intersection(p[j])) >= k:
                    g[i].append(j)
                    g[j].append(i)
        v = [False] * n
        def dfs(u):
            v[u] = True
            for w in g[u]:
                if not v[w]:
                    dfs(w)
        comp = 0
        for i in range(n):
            if not v[i]:
                comp += 1
                dfs(i)
        return comp