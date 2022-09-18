class Solution:
    def DFS(self, graph, i, dest, v):
        if i == dest:
            return True
        v.add(i)
        for j in graph[i]:
            if j not in v:
                if self.DFS(graph, j, dest, v):
                    return True
        return False
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        v = set()
        return self.DFS(graph, source, destination, v)