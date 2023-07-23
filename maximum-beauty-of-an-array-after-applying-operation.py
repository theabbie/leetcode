class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        res = 1
        for j in range(n):
            while i < j and nums[i] + k < nums[j] - k:
                i += 1
            if nums[i] + k >= nums[j] - k:
                res = max(res, j - i + 1)
        return res