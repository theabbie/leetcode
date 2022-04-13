import heapq

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evens = []
        odds = []
        for i in range(n):
            if i & 1:
                heapq.heappush(odds, -nums[i])
            else:
                heapq.heappush(evens, nums[i])
        for i in range(n):
            if i & 1:
                nums[i] = -heapq.heappop(odds)
            else:
                nums[i] = heapq.heappop(evens)
        return nums