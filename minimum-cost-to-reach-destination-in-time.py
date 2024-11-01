class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = defaultdict(lambda: float('inf'))
        dist[(0, maxTime)] = passingFees[0]
        heap = [(passingFees[0], 0, maxTime)]
        while heap:
            cost, i, rem = heapq.heappop(heap)
            if i == n - 1:
                return cost
            for j, w in graph[i]:
                if w <= rem:
                    if dist[(j, rem - w)] > cost + passingFees[j]:
                        dist[(j, rem - w)] = cost + passingFees[j]
                        heapq.heappush(heap, (cost + passingFees[j], j, rem - w))
        return -1