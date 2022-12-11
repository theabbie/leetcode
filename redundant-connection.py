from collections import defaultdict

class Solution:
    def DFS(self, graph, i, v, a, b):
        for j in graph[i]:
            if j not in v and (i, j) != (a, b) and (i, j) != (b, a):
                v.add(j)
                self.DFS(graph, j, v, a, b)
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        for a, b in edges[::-1]:
            v = {a}
            self.DFS(graph, a, v, a, b)
            if len(v) == len(graph):
                return [a, b]