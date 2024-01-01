class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            ctr = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                i += 1
            if nums[i] == 0:
                res += ctr * (ctr + 1) // 2
            i += 1
        return res