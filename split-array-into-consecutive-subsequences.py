from collections import defaultdict
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        numctr = defaultdict(list)
        for val in nums:
            l = 0
            currheap = numctr[val]
            if (val - 1) in numctr:
                prevheap = numctr[val - 1]
                if len(prevheap) > 0:
                    l = heapq.heappop(prevheap)
            heapq.heappush(currheap, 1 + l)
        for val in numctr:
            if len(numctr[val]) > 0 and numctr[val][0] < 3:
                return False
        return True