class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        j = i - 1
        res = []
        while i < len(nums) and j >= 0:
            if nums[i] * nums[i] <= nums[j] * nums[j]:
                res.append(nums[i] * nums[i])
                i += 1
            else:
                res.append(nums[j] * nums[j])
                j -= 1
        while i < len(nums):
            res.append(nums[i] * nums[i])
            i += 1
        while j >= 0:
            res.append(nums[j] * nums[j])
            j -= 1
        return res