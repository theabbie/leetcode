class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        cache = {}
        def dfs(graph, i, prev, XOR):
            val = nums[i]
            if XOR:
                val ^= k
            key = (i, prev, XOR)
            if key in cache:
                return cache[key]
            X = []
            nb = 0
            for j in graph[i]:
                if j == prev:
                    continue
                nb += 1
                X.append([dfs(graph, j, i, True), dfs(graph, j, i, False)])
            X.sort(key = lambda p: (p[1] - p[0], p[1]))
            X.insert(0, [0, 0])
            for j in range(len(X) - 1):
                X[j + 1][0] += X[j][0]
                X[j + 1][1] += X[j][1]
            maxnb = float('-inf')
            choose = 0
            while choose <= nb:
                maxnb = max(maxnb, X[choose][0] + X[nb][1] - X[choose][1])
                choose += 2
            maxnbifFlip = float('-inf')
            choose = 1
            while choose <= nb:
                maxnbifFlip = max(maxnbifFlip, X[choose][0] + X[nb][1] - X[choose][1])
                choose += 2
            res = max(val + maxnb, (val ^ k) + maxnbifFlip)
            cache[key] = res
            return res
        return dfs(graph, 0, -1, False)