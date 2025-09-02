import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        res = 0
        i = 0
        for t in range(min(e[0] for e in events), max(e[1] for e in events) + 1):
            while i < len(events) and events[i][0] <= t:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < t:
                heapq.heappop(heap)
            if heap:
                res += 1
                heapq.heappop(heap)
        return res