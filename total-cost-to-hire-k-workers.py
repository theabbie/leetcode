import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if n <= 2 * candidates:
            res = 0
            costs.sort()
            for i in range(k):
                res += costs[i]
            return res
        heapl = []
        heapr = []
        i = None
        j = None
        for x in range(candidates):
            if x < n - x - 1:
                i = x + 1
                j = n - x - 2
                heapq.heappush(heapl, (costs[x], x))
                heapq.heappush(heapr, (costs[n - x - 1], n - x - 1))
        res = 0
        for _ in range(k):
            if len(heapl) > 0 and len(heapr) > 0 and heapl[0][0] <= heapr[0][0]:
                curr = heapq.heappop(heapl)
                res += curr[0]
                if i <= j:
                    heapq.heappush(heapl, (costs[i], i))
                    i += 1
            elif len(heapr) > 0:
                curr = heapq.heappop(heapr)
                res += curr[0]
                if j >= i:
                    heapq.heappush(heapr, (costs[j], j))
                    j -= 1
        return res