from collections import defaultdict

class Solution:
    def DFS(self, i, graph, v):
        v.add(i)
        for j in graph[i]:
            if j not in v:
                self.DFS(j, graph, v)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        v = set()
        ctr = 0
        for i in range(n):
            if i not in v:
                self.DFS(i, graph, v)
                ctr += 1
        return ctr