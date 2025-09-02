class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(int(nums[i] == 2 * nums[i - 1] + 2 * nums[i + 1]) for i in range(1, len(nums) - 1))