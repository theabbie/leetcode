from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add((b, 1))
            graph[b].add((a, 0))
        res = 0
        q = deque([(0, -1)])
        while len(q) > 0:
            i, prev = q.pop()
            for j, c in graph[i]:
                if j != prev:
                    res += c
                    q.appendleft((j, i))
        return res