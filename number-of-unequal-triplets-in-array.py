class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                i += 1
            i += 1
            res += (i - ctr) * ctr * (n - i)
        return res