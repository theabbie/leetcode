from collections import defaultdict

class Solution:
    def DFS(self, graph, i, visited):
        for j in graph[i]:
            if j not in visited:
                self.ctr += 1
                visited.add(j)
                self.DFS(graph, j, visited)
    
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        total = 0
        res = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                self.ctr = 1
                self.DFS(graph, i, visited)
                res += self.ctr * total
                total += self.ctr
        return res