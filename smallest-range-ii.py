class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[-1] - nums[0]
        left = nums[0] + k
        right = nums[-1] - k
        for i in range(n - 1):
            currmax = max(right, nums[i] + k)
            currmin = min(left, nums[i + 1] - k)
            res = min(res, currmax - currmin)
        return res