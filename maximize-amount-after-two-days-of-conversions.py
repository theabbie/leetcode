from collections import defaultdict
import heapq

class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        graph = defaultdict(set)
        for i in range(len(pairs1)):
            graph[(pairs1[i][0], 0)].add((pairs1[i][1], 0, rates1[i]))
            graph[(pairs1[i][1], 0)].add((pairs1[i][0], 0, 1 / rates1[i]))
        for i in range(len(pairs2)):
            graph[(pairs2[i][0], 1)].add((pairs2[i][1], 1, rates2[i]))
            graph[(pairs2[i][1], 1)].add((pairs2[i][0], 1, 1 / rates2[i]))
        for curr in list(graph):
            graph[(curr[0], 0)].add((curr[0], 1, 1))
        dist = defaultdict(lambda: float('-inf'))
        heap = [(-1, initialCurrency, 0)]
        dist[(initialCurrency, 0)] = 1
        res = 1
        while heap:
            d, curr, day = heapq.heappop(heap)
            d = -d
            if curr == initialCurrency:
                res = max(res, d)
            for j, jd, jr in graph[(curr, day)]:
                if dist[(j, jd)] < d * jr:
                    dist[(j, jd)] = d * jr
                    heapq.heappush(heap, (-dist[(j, jd)], j, jd))
        return res