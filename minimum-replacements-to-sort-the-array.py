import math

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                k = math.ceil(nums[i] / nums[i + 1])
                res += k - 1
                nums[i] //= k
        return res