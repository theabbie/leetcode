from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        g = defaultdict(set)
        indegree = [0] * n
        for i in range(n):
            for j in graph[i]:
                g[j].add(i)
                indegree[i] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.appendleft(i)
        res = []
        while len(q) > 0:
            curr = q.pop()
            res.append(curr)
            for j in g[curr]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.appendleft(j)
        res.sort()
        return res