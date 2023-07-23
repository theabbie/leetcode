class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = max(nums)
        while len(nums) > 1:
            if nums[-1] >= nums[-2]:
                nums[-2] += nums[-1]
                nums.pop()
            else:
                res = max(res, nums.pop())
        return max(nums + [res])