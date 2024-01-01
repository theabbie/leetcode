from collections import defaultdict

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        m = min(nums)
        M = max(nums)
        graph = defaultdict(set)
        latest = defaultdict(list)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        res = [-1] * n
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def dfs(graph, curr, prev, d):
            maxdepth = (-1, -1)
            for g in range(m, M + 1):
                if gcd(nums[curr], g) == 1 and len(latest[g]) > 0:
                    maxdepth = max(maxdepth, latest[g][-1])
            res[curr] = maxdepth[1]
            for j in graph[curr]:
                if j == prev:
                    continue
                latest[nums[curr]].append((d, curr))
                dfs(graph, j, curr, d + 1)
                latest[nums[curr]].pop()
        dfs(graph, 0, -1, 0)
        return res