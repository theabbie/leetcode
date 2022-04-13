class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i == n - 1 or nums[i] != nums[i + 1]:
                nums.append(nums[i])
        del nums[:n]