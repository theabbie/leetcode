class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        x = set(nums)
        n = len(nums)
        s = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1
        res = s
        while res in x:
            res += 1
        return res