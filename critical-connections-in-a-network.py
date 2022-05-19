from collections import defaultdict

class Solution:
    def DFS(self, graph, node, v, parent, disc, low):
        v.add(node)
        disc[node] = self.t
        low[node] = self.t
        self.t += 1
        for j in graph[node]:
            if j not in v:
                parent[j] = node
                self.DFS(graph, j, v, parent, disc, low)
                low[node] = min(low[node], low[j])
            elif j != parent[node]:
                low[node] = min(low[node], disc[j])
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        self.t = 0
        parent = defaultdict(lambda: -1)
        disc = defaultdict(lambda: float('inf'))
        low = defaultdict(lambda: float('inf'))
        v = set()
        for i in range(n):
            if i not in v:
                self.DFS(graph, i, v, parent, disc, low)
        return [[u, v] for u, v in connections if low[u] > disc[v] or low[v] > disc[u]]