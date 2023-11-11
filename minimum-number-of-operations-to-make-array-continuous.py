from bisect import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        vals = sorted(set(nums))
        def minops(beg):
            return n - bisect_right(vals, beg + n - 1) + bisect_left(vals, beg)
        res = n - 1
        for i in range(n):
            res = min(res, minops(nums[i]), minops(nums[i] - i))
        return res