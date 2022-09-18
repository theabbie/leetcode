import math

class Solution:
    def isPossible(self, nums, maxOperations, l):
        curr = 0
        for b in nums:
            curr += math.ceil(b / l) - 1
        return curr <= maxOperations
    
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        beg = 1
        end = max(nums)
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.isPossible(nums, maxOperations, mid):
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res