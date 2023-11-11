class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + nums
        for i in range(n):
            if nums[n - i : 2 * n - i] == sorted(nums[n - i : 2 * n - i]):
                return i
        return -1