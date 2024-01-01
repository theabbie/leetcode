from collections import defaultdict, deque

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        res = float('inf')
        for a, b in edges:
            q = deque([(a, 0)])
            v = {a}
            while len(q) > 0:
                curr, d = q.pop()
                if curr == b:
                    res = min(res, d + 1)
                for j in graph[curr]:
                    if j not in v and (curr, j) not in {(a, b), (b, a)}:
                        v.add(j)
                        q.appendleft((j, d + 1))
        if res == float('inf'):
            return -1
        return res