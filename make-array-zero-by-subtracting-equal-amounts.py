class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        curr = 0
        res = 0
        for i in range(n):
            if nums[i] > curr:
                res += 1
                curr = nums[i]
        return res