class Solution:
    def deleteTreeNodes(self, n: int, parent: List[int], value: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)
        def dfs(i):
            s = value[i]
            ctr = 1
            for j in graph[i]:
                cs, cctr = dfs(j)
                s += cs
                ctr += cctr
            if s == 0:
                ctr = 0
            return s, ctr
        return dfs(0)[1]