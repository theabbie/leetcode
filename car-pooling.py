import bisect

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        points = []
        for i in range(n):
            num, source, dest = trips[i]
            bisect.insort(points, (source, num))
            bisect.insort(points, (dest, -num))
        k = len(points)
        curr = 0
        for i in range(k):
            curr += points[i][1]
            if curr > capacity:
                return False
        return True