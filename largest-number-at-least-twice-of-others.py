class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        currmax = max(range(n), key = lambda i: nums[i])
        nums.sort()
        return currmax if nums[-1] >= 2 * nums[-2] else -1