from collections import defaultdict

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        graph = defaultdict(set)
        for r in regions:
            for i in range(1, len(r)):
                graph[r[0]].add(r[i])
        res = -1
        v = set()
        def dfs(x):
            has = False
            ctr = 0
            nonlocal res
            if x == region1 or x == region2:
                has = True
                ctr += 1
            for y in graph.get(x, []):
                if y not in v:
                    v.add(y)
                    childhas = dfs(y)
                    if childhas:
                        has = True
                        ctr += 1
            if ctr >= 2:
                res = x
            return has
        for el in graph:
            if el not in v:
                v.add(el)
                dfs(el)
        return res