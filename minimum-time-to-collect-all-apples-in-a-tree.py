from collections import defaultdict

class Solution:
    def gettime(self, graph, curr, prev, hasApple):
        res = 0
        for j in graph[curr]:
            if j != prev:
                currtime = self.gettime(graph, j, curr, hasApple)
                if currtime > 0 or hasApple[j]:
                    res += 2 + currtime
        return res
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return self.gettime(graph, 0, -1, hasApple)