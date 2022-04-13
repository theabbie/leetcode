class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lc = 1
        lp = [lc]
        rc = 1
        rp = [rc]
        for i in range(n):
            lc *= nums[i]
            lp.append(lc)
            rc *= nums[n - i - 1]
            rp.append(rc)
        return [lp[i] * rp[n - i - 1] for i in range(n)]