class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        for i in range(0, n, 2):
            total += min(nums[i:i + 2])
        return total