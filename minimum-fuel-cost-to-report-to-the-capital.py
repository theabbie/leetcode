from collections import defaultdict
import math

class Solution:
    def DFS(self, graph, i, prev, seats):
        size = 1
        for j in graph[i]:
            if j != prev:
                size += self.DFS(graph, j, i, seats)
        if i != 0:
            self.res += math.ceil(size / seats)
        return size
    
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        self.res = 0
        self.DFS(graph, 0, -1, seats)
        return self.res