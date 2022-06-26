import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = []
        total = 0
        for i, el in enumerate(target):
            if el > 1:
                heapq.heappush(heap, -el)
            total += el
        while len(heap) > 0:
            largest = -heapq.heappop(heap)
            if total >= 2 * largest or total - largest == 0:
                return False
            newval = largest % (total - largest)
            if newval == 0:
                newval += total - largest
            total = total - largest + newval
            if newval > 1:
                heapq.heappush(heap, -newval)
        return True