class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        depth = [0] * n
        stack = [(0, 0, -1)]
        while stack:
            i, d, p = stack.pop()
            parent[i] = p
            depth[i] = d
            for j in graph[i]:
                if j != p:
                    stack.append((j, d + 1, i))
        res = []
        for u, v, target in query:
            q = deque()
            vs = set()
            while u != -1 and v != -1 and u != v:
                if depth[u] < depth[v]:
                    u, v = v, u
                q.appendleft((u, u))
                vs.add(u)
                u = parent[u]
            if u == v and u != -1:
                if u not in vs:
                    vs.add(u)
                    q.appendleft((u, u))
            while q:
                src, i = q.pop()
                if i == target:
                    res.append(src)
                    break
                for j in graph[i]:
                    if j not in vs:
                        vs.add(j)
                        q.appendleft((src, j))
        return res