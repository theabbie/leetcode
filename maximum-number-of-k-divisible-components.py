from collections import defaultdict

class Solution:
    def maxsplits(self, graph, i, prev, k, values):
        res = 0
        curr = values[i]
        res = 0
        for j in graph[i]:
            if j != prev:
                ncurr, nres = self.maxsplits(graph, j, i, k, values)
                curr += ncurr
                curr %= k
                res += nres
        if curr % k == 0:
            res += 1
            curr = 0
        return curr, res
    
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        return self.maxsplits(graph, 0, -1, k, values)[1]