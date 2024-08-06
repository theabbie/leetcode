class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        @lru_cache(maxsize = None)
        def p(i, pv, rem):
            if rem < 0:
                return 0
            leaf = True
            for j in graph[i]:
                if j != pv:
                    leaf = False
            if i == target - 1:
                if rem > 0 and not leaf:
                    return 0
                else:
                    return 1
            if rem == 0:
                return 0
            s = 0
            ctr = 0
            for j in graph[i]:
                if j != pv:
                    s += p(j, i, rem - 1)
                    ctr += 1
            if ctr == 0:
                return 0
            return s / ctr
        return p(0, -1, t)