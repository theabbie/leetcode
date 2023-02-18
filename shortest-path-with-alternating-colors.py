from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in redEdges:
            graph[u].add((v, 0))
        for u, v in blueEdges:
            graph[u].add((v, 1))
        res = [-1] * n
        q = deque([(0, -1, 0)])
        v = {(0, -1)}
        while len(q) > 0:
            curr, prev, d = q.pop()
            if res[curr] == -1 or d < res[curr]:
                res[curr] = d
            for j, c in graph[curr]:
                if c != prev and (j, c) not in v:
                    v.add((j, c))
                    q.appendleft((j, c, d + 1))
        return res