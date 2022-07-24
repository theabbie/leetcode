class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                i += 1
            i += 1
            if nums[i - 1] == 0:
                res += ctr * (ctr + 1) // 2
        return res