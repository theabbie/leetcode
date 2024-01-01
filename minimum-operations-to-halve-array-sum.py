import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        s = 0
        for el in nums:
            heapq.heappush(heap, -el)
            s += el
        curr = s
        res = 0
        while 2 * curr > s:
            el = -heapq.heappop(heap)
            curr -= el / 2
            res += 1
            heapq.heappush(heap, -el / 2)
        return res