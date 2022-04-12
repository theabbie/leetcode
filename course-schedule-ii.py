class Solution:
    def topologicalSort(self, graph, node, visited):
        visited.add(node)
        for j in graph.get(node, []):
            if j not in visited:
                self.topologicalSort(graph, j, visited)
        self.sorted.append(node)
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in prerequisites:
            graph[b] = graph.get(b, []) + [a]
        self.sorted = []
        visited = set()
        for node in range(numCourses):
            if node not in visited:
                self.topologicalSort(graph, node, visited)
        self.sorted.reverse()
        pos = {}
        for i, node in enumerate(self.sorted):
            pos[node] = i
        for i in graph:
            for j in graph[i]:
                if pos[i] > pos[j]:
                    return []
        return self.sorted