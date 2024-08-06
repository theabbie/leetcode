class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        res = [[i] for i in range(n)]
        v = [False] * n
        for a, b in edges:
            graph[b].append(a)
        def merge(x, y):
            merged = []
            i, j = 0, 0
            while i < len(x) and j < len(y):
                if x[i] < y[j]:
                    merged.append(x[i])
                    i += 1
                elif x[i] > y[j]:
                    merged.append(y[j])
                    j += 1
                else:
                    merged.append(x[i])
                    i += 1
                    j += 1
            while i < len(x):
                merged.append(x[i])
                i += 1
            while j < len(y):
                merged.append(y[j])
                j += 1
            return merged
        def f(i):
            if v[i]:
                return
            v[i] = True
            for j in graph[i]:
                f(j)
                res[i] = merge(res[i], res[j])
        for i in range(n):
            f(i)
        for i in range(n):
            res[i].remove(i)
        return res