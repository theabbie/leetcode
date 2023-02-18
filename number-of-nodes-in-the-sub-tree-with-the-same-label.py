from collections import defaultdict, Counter

class Solution:
    def DFS(self, graph, i, prev, labels):
        ctr = Counter()
        ctr[labels[i]] += 1
        for j in graph[i]:
            if j != prev:
                ctr += self.DFS(graph, j, i, labels)
        self.res[i] = ctr[labels[i]]
        return ctr
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        self.res = [0] * n
        self.DFS(graph, 0, -1, labels)
        return self.res