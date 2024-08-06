import heapq

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, ctr in edges:
            graph[u].append((v, ctr + 1))
            graph[v].append((u, ctr + 1))
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]
        while heap:
            d, curr = heapq.heappop(heap)
            for j, w in graph[curr]:
                if dist[j] > d + w:
                    dist[j] = d + w
                    heapq.heappush(heap, (dist[j], j))
        res = 0
        for i in range(n):
            if dist[i] <= maxMoves:
                res += 1
        for u, v, ctr in edges:
            left = max(maxMoves - dist[u], 0)
            right = max(maxMoves - dist[v], 0)
            res += min(left + right, ctr)
        return res