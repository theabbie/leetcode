from collections import deque

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        v = [False] * n
        q = deque()
        def dfs(i, p):
            q.appendleft((i, 0))
            v[i] = True
            for j in graph[i]:
                if not v[j]:
                    if dfs(j, i):
                        return True
                elif j != p:
                    while q and q[-1][0] != j:
                        q.pop()
                    return True
            q.popleft()
            v[i] = False
            return False
        dfs(0, -1)
        v = [False] * n
        for i, d in q:
            v[i] = True
        res = [0] * n
        while q:
            i, d = q.pop()
            res[i] = d
            for j in graph[i]:
                if not v[j]:
                    v[j] = True
                    q.appendleft((j, d + 1))
        return res