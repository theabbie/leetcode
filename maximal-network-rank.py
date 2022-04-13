from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        l = len(roads)
        edges = defaultdict(set)
        for k in range(l):
            a, b = roads[k]
            edges[a].add(k)
            edges[b].add(k)
        mnetwork = 0
        for i in range(n):
            for j in range(i + 1, n):
                mnetwork = max(mnetwork, len(set.union(edges[i], edges[j])))
        return mnetwork