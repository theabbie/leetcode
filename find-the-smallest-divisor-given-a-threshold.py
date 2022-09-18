import math

class Solution:
    def getSum(self, nums, d):
        val = 0
        if d == 0:
            return float('inf')
        for num in nums:
            val += math.ceil(num / d)
        return val
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        end = 1
        while self.getSum(nums, end) > threshold:
            end *= 2
        beg = end // 2
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if self.getSum(nums, mid) <= threshold:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res