class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] <= 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        for j in range(i, n):
            if 1 <= abs(nums[j]) <= n - i:
                nums[i + abs(nums[j]) - 1] = -abs(nums[i + abs(nums[j]) - 1])
        for j in range(i, n):
            if nums[j] > 0:
                return j - i + 1
        return n - i + 1