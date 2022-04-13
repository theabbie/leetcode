class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {}
        for a, b in edges:
            if a in graph:
                graph[a][0] += 1
                graph[a][1] += 1
            else:
                graph[a] = [1, 1]
            if b in graph:
                graph[b][1] += 1
                graph[a][0] += 1
            else:
                graph[b] = [1, 1]
        for node in graph:
            if graph[node][1] == len(graph) - 1:
                return node