class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i > 0:
            fn = lambda k: (float('inf') if nums[k] <= nums[i - 1] else nums[k], -k)
            closest = min(range(i, n), key = fn)
            nums[i - 1], nums[closest] = nums[closest], nums[i - 1]
        for p in range((n - i) // 2):
            nums[i + p], nums[n - p - 1] = nums[n - p - 1], nums[i + p]