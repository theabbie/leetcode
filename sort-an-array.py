import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heapq.heapify(nums)
        return heapq.nsmallest(n, nums)