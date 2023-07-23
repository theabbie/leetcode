import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap = []
        i = 0
        j = n - 1
        for _ in range(candidates):
            if i <= j:
                heapq.heappush(heap, (costs[i], i, True))
                i += 1
                if i <= j:
                    heapq.heappush(heap, (costs[j], j, False))
                    j -= 1
        res = 0
        for _ in range(k):
            curr, pos, left = heapq.heappop(heap)
            res += curr
            if left and i <= j:
                heapq.heappush(heap, (costs[i], i, True))
                i += 1
            if not left and i <= j:
                heapq.heappush(heap, (costs[j], j, False))
                j -= 1
        return res