class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            x = nums[i]
            b = 0
            while nums[i] & (1 << b):
                b += 1
            if b:
                x &= ~(1 << (b - 1))
            if x | (x + 1) == nums[i]:
                nums[i] = x
            else:
                nums[i] = -1
        return nums