from collections import *

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(s)
        graph = defaultdict(set)
        for i in range(n):
            if parent[i] != -1:
                graph[parent[i]].add(i)
        q = deque([0])
        topo = []
        while len(q) > 0:
            curr = q.pop()
            topo.append(curr)
            for j in graph[curr]:
                q.appendleft(j)
        topo.reverse()
        res = 0
        longest = [1] * n
        for i in topo:
            a, b = 0, 0
            for j in graph[i]:
                if s[j] != s[i]:
                    longest[i] = max(longest[i], 1 + longest[j])
                    temp, a, b = sorted([a, b, longest[j]])
            res = max(res, a + b + 1)
        return res