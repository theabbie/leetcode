import heapq
from collections import defaultdict

class Solution:
    def union(self, parent, i, j):
        parent[i] = j
        
    def getParent(self, parent, i):
        if i not in parent:
            return i
        return self.getParent(parent, parent[i])
        
    def isCycle(self, graph, n):
        parent = {}
        for i in graph:
            for j in graph[i]:
                x = self.getParent(parent, i)
                y = self.getParent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False
    
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                a, b = points[i]
                c, d = points[j]
                cost = abs(c - a) + abs(d - b)
                heapq.heappush(edges, (cost, i, j))
        graph = defaultdict(set)
        rem = n - 1
        op = 0
        while rem > 0:
            if len(edges) > 0:
                currdist, i, j = heapq.heappop(edges)
                graph[i].add(j)
                if self.isCycle(graph, n):
                    graph[i].remove(j)
                else:
                    rem -= 1
                    op += currdist
        return op