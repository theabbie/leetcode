from collections import defaultdict

class Solution:
    def DFS(self, i, graph, v):
        for j in graph[i]:
            if j not in v:
                v.add(j)
                self.DFS(j, graph, v)
    
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        v = set([0] + restricted)
        self.DFS(0, graph, v)
        return len(v) - len(restricted)