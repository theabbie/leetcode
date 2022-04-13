import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        points = []
        for i in range(n):
            num, source, dest = trips[i]
            heapq.heappush(points, (source, num))
            heapq.heappush(points, (dest, -num))
        curr = 0
        while len(points) > 0:
            curr += heapq.heappop(points)[1]
            if curr > capacity:
                return False
        return True