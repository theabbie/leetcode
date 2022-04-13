class Solution:
    def DFS(self, graph, curr, visited, colors):
        for j in graph[curr]:
            if j not in visited:
                visited.add(j)
                colors[j] = not colors[curr]
                if not self.DFS(graph, j, visited, colors):
                    return False
            else:
                if colors[j] == colors[curr]:
                    return False
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        for i in range(n):
            colors = [False for node in graph]
            visited = {i}
            if not self.DFS(graph, i, visited, colors):
                return False
        return True