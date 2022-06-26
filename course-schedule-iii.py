import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        courses.sort(key = lambda c: (c[1], c[0]))
        ctr = 0
        prev = 0
        heap = []
        for i in range(n):
            duration, deadline = courses[i]
            if prev + duration <= deadline:
                ctr += 1
                prev += duration
                heapq.heappush(heap, -duration)
            elif len(heap) > 0:
                largest = -heap[0]
                if duration < largest and prev - largest + duration <= deadline:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -duration)
                    prev -= (largest - duration)
        return ctr