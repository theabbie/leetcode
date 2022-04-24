from collections import defaultdict

class Solution:
    def getPath(self, node, graph, visited, time, values, maxTime):
        if node == 0:
            currQuality = sum([values[i] for i in visited])
            if currQuality >= self.maxQuality:
                self.maxQuality = currQuality
        for j, t in graph[node]:
            if time + t <= maxTime:
                self.getPath(j, graph, visited.union({j}), time + t, values, maxTime)
    
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.maxQuality = float('-inf')
        graph = defaultdict(list)
        for a, b, t in edges:
            graph[a].append((b, t))
            graph[b].append((a, t))
        self.getPath(0, graph, {0}, 0, values, maxTime)
        return self.maxQuality