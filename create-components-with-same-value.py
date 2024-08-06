from collections import *

class Solution:
    def maxsplits(self, graph, i, prev, k, values):
        res = 0
        curr = values[i]
        res = 0
        for j in graph[i]:
            if j != prev:
                ncurr, nres = self.maxsplits(graph, j, i, k, values)
                curr += ncurr
                res += nres
        if curr == k:
            res += 1
            curr = 0
        return curr, res
    
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        res = 0
        total = sum(nums)
        s = 1
        while s * s <= total:
            if total % s == 0:
                x = self.maxsplits(graph, 0, -1, s, nums)
                if x[0] == 0:
                    res = max(res, x[1] - 1)
                if s * s < total:
                    x = self.maxsplits(graph, 0, -1, total // s, nums)
                    if x[0] == 0:
                        res = max(res, x[1] - 1)
            s += 1
        return res