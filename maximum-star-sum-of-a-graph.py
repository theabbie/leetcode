from collections import defaultdict

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for i in range(len(vals)):
            graph[i] = []
        for a, b in edges:
            graph[a].append((b, vals[b]))
            graph[b].append((a, vals[a]))
        res = float('-inf')
        for el in graph:
            curr = vals[el]
            nb = []
            for j, c in graph[el]:
                nb.append(c)
            nb.sort(reverse = True)
            for i in range(min(len(nb), k)):
                curr += max(nb[i], 0)
            res = max(res, curr)
        return res