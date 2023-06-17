from collections import defaultdict, deque, Counter

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(set)
        indegree = [0] * n
        for a, b in edges:
            graph[a].add(b)
            indegree[b] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.appendleft(i)
        ctr = [Counter() for _ in range(n)]
        res = 0
        l = 0
        while len(q) > 0:
            curr = q.pop()
            l += 1
            ctr[curr][colors[curr]] += 1
            res = max(res, ctr[curr][colors[curr]])
            for j in graph[curr]:
                for cc in range(26):
                    c = chr(ord('a') + cc)
                    ctr[j][c] = max(ctr[j][c], ctr[curr][c])
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.appendleft(j)
        if l < n:
            return -1
        return res