from collections import deque

class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        indegree = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            a -= 1
            b -= 1
            graph[a].append(b)
            indegree[b] += 1
        z = indegree.count(0)
        for a, b in edges[::-1]:
            a -= 1
            b -= 1
            if z + int(indegree[b] == 1) != 1:
                continue
            deg = indegree[:]
            deg[b] -= 1
            q = deque()
            ctr = 0
            for i in range(n):
                if deg[i] == 0:
                    q.appendleft(i)
            while len(q) > 0:
                curr = q.pop()
                ctr += 1
                for j in graph[curr]:
                    if (curr, j) == (a, b):
                        continue
                    deg[j] -= 1
                    if deg[j] == 0:
                        q.appendleft(j)
            if ctr == n:
                return [a + 1, b + 1]