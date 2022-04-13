import heapq

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        heapq.heapify(nums)
        curr = heapq.heappop(nums)
        for _ in range(n - 1):
            currnew = heapq.heappop(nums)
            if curr == currnew:
                return True
            curr = currnew
        return False