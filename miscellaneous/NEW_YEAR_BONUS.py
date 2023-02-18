from collections import defaultdict

t = int(input())

class Solver:
    def DFS(self, graph, i, v):
        ctr = 1
        s = 0
        for j in graph[i]:
            if j not in v:
                v.add(j)
                currctr, currs = self.DFS(graph, j, v)
                ctr += currctr
                s += currs + currctr
        self.count[i] = ctr
        return (ctr, s)
    
    def solve(self, n, edges):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        self.count = [0] * n
        res = [0] * n
        res[0] = self.DFS(graph, 0, {0})[1]
        stack = [0]
        v = {0}
        while len(stack) > 0:
            i = stack.pop()
            for j in graph[i]:
                if j not in v:
                    v.add(j)
                    stack.append(j)
                    res[j] = n + res[i] - 2 * self.count[j]
        ctr = 0
        a, b = min(res), max(res)
        for el in res:
            if 2 * el < a + b:
                ctr += 1
        return ctr

for _ in range(t):
    n = int(input())
    edges = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    print(Solver().solve(n, edges))