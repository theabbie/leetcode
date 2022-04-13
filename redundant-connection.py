class Solution:
    def DFS(self, node, graph, visited, src, dest):
        visited.add(node)
        for i in graph.get(node, []):
            if i not in visited:
                if (node, i) != (src, dest) and (i, node) != (dest, src):
                    self.DFS(i, graph, visited, src, dest)
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = {}
        numnodes = 0
        for a, b in edges:
            numnodes = max(numnodes, a, b)
            graph[a] = graph.get(a, set()).union({b})
            graph[b] = graph.get(b, set()).union({a})
        for k in range(n - 1, -1, -1):
            a, b = edges[k]
            visited = set()
            self.DFS(a, graph, visited, a, b)
            if len(visited) == numnodes:
                return edges[k]