import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []
        res = 0
        i = 0
        while i < n or heap:
            while heap and heap[0][0] < i:
                heapq.heappop(heap)
            if i < n and days[i] > 0:
                heapq.heappush(heap, (i + days[i] - 1, apples[i]))
            if heap:
                end, ctr = heapq.heappop(heap)
                res += 1
                if ctr - 1 > 0:
                    heapq.heappush(heap, (end, ctr - 1))
            i += 1
        return res