from collections import defaultdict

class Solution:
    def DFS(self, graph, i, v):
        for j in graph[i]:
            self.edges.add((min(i, j), max(i, j)))
            if j not in v:
                v.add(j)
                self.DFS(graph, j, v)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        ctr = 0
        extra = 0
        v = set()
        for i in range(n):
            if i not in v:
                ctr += 1
                currv = {i}
                self.edges = set()
                self.DFS(graph, i, currv)
                extra += len(self.edges) - len(currv) + 1
                v.update(currv)
        if extra < ctr - 1:
            return -1
        return ctr - 1