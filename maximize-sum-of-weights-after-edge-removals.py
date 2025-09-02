class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        cache = [[-1] * 2 for _ in range(n)]
        def minsum(i, p, hasparent):
            if cache[i][int(hasparent)] != -1:
                return cache[i][int(hasparent)]
            childs = []
            for j, w in graph[i]:
                if j == p:
                    continue
                childs.append((w + minsum(j, i, True), minsum(j, i, False)))
            childs.sort(key = lambda p: p[1] - p[0])
            total = 0
            for x, y in childs:
                total += y
            res = total
            take = k
            if hasparent:
                take = k - 1
            taken = 0
            for j in range(take):
                if j >= len(childs):
                    break
                taken += childs[j][0]
                total -= childs[j][1]
                res = max(res, taken + total)
            cache[i][int(hasparent)] = res
            return res
        return minsum(0, -1, False)