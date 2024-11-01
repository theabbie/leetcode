class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = 1 + len(edges)
        graph = [[] for _ in range(n)]
        guess = [set() for _ in range(n)]
        for u, v in guesses:
            guess[u].add(v)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def subdfs(i, p):
            s = int(p in guess[i])
            for j in graph[i]:
                if j != p:
                    s += subdfs(j, i)
            return s
        res = [0] * n
        res[0] = len(guesses) - subdfs(0, -1)
        def dfs(i, p):
            for j in graph[i]:
                if j != p:
                    res[j] = res[i] - int(j in guess[i]) + int(i in guess[j])
                    dfs(j, i)
        dfs(0, -1)
        return sum(1 for el in res if el >= k)