from collections import deque, defaultdict

class Solution:
    def bfs(self, graph, root, parent):
        q = deque([root])
        v = {root}
        while len(q) > 0:
            curr = q.pop()
            for j in graph[curr]:
                if j not in v:
                    v.add(j)
                    parent[j] = curr
                    q.appendleft(j)
    
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        parent = {}
        self.bfs(graph, bob, parent)
        curr = 0
        path = [curr]
        while curr in parent:
            curr = parent[curr]
            path.append(curr)
        path.reverse()
        exists = [0]
        for i in range(len(path) - 1):
            exists.append(exists[-1])
            exists[-1] |= 1 << path[i]
        q = deque([(0, 0, 0)])
        v = {0}
        res = float('-inf')
        while len(q) > 0:
            curr, t, cost = q.pop()
            c = amount[curr]
            if t < len(path):
                if path[t] == curr:
                    c //= 2
                elif exists[t] & (1 << curr):
                    c = 0
            if len(graph[curr]) == 1 and curr != 0:
                res = max(res, cost + c)
            for j in graph[curr]:
                if j not in v:
                    v.add(j)
                    q.appendleft((j, t + 1, cost + c))
        return res