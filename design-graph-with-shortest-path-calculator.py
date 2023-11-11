from collections import *
import heapq

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(set)
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].add((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = defaultdict(lambda: float('inf'))
        dist[node1] = 0
        heap = [(dist[node1], node1)]
        while len(heap) > 0:
            currd, node = heapq.heappop(heap)
            if node == node2:
                return currd
            for j, w in self.graph[node]:
                if dist[j] > currd + w:
                    dist[j] = currd + w
                    heapq.heappush(heap, (dist[j], j))
        return -1