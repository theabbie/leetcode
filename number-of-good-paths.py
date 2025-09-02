from sortedcontainers import SortedList

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        sizes = [0] * n

        def dfs(i, prev):
            sizes[i] = 1
            for j in graph[i]:
                if j != prev:
                    sizes[i] += dfs(j, i)
            return sizes[i]
        
        def getcentroid(i, prev, total):
            for j in graph[i]:
                if j != prev and sizes[j] > total // 2:
                    return getcentroid(j, i, total)
            return i
        
        def solve(i):
            total = dfs(i, -1)
            centroid = getcentroid(i, -1, total)
            ctr = defaultdict(SortedList)

            res = 1
            
            def find(x, prev, mx, store):
                nonlocal ctr, res
                if not store and vals[x] == vals[centroid] and mx <= vals[x]:
                    res += 1
                if x != centroid and store and mx <= vals[x]:
                    ctr[vals[x]].add(mx)
                elif x != centroid and mx <= vals[x]:
                    res += ctr[vals[x]].bisect_right(mx)
                for y in graph[x]:
                    if y != prev:
                        find(y, x, max(mx, vals[y]), store)

            for j in graph[centroid]:
                mx = max(vals[centroid], vals[j])
                find(j, centroid, mx, False)
                find(j, centroid, mx, True)
            
            for j in list(graph[centroid]):
                graph[centroid].remove(j)
                graph[j].remove(centroid)
                res += solve(j)
            
            return res

        return solve(0)