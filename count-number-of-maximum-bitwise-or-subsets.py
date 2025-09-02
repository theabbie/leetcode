class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for el in nums:
            target |= el
        @cache
        def dp(i, x):
            if i >= len(nums):
                return int(x == target)
            return dp(i + 1, x) + dp(i + 1, x | nums[i])
        return dp(0, 0)