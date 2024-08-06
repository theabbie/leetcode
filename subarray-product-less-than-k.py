class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        i = 0
        s = 1
        for j in range(len(nums)):
            s *= nums[j]
            while i <= j and s >= k:
                s //= nums[i]
                i += 1
            res += j - i + 1
        return res