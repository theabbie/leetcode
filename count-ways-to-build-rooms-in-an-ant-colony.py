from collections import *

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(prevRoom)
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = i * f[i - 1]
            f[i] %= M
        count = lambda x, y: (f[x + y] * pow(f[x] * f[y], M - 2, M)) % M
        graph = [[] for _ in range(n)]
        for i in range(n):
            if prevRoom[i] != -1:
                graph[prevRoom[i]].append(i)
        def dfs(i):
            curr = 1
            s = 0
            for j in graph[i]:
                ctr, cs = dfs(j)
                curr *= count(s, cs) * ctr
                curr %= M
                s += cs
            s += 1
            return curr, s
        return dfs(0)[0]