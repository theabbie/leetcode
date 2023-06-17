class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        minpos = maxpos = n
        res = 0
        lastout = n
        for i in range(n - 1, -1, -1):
            if nums[i] == minK:
                minpos = i
            if nums[i] == maxK:
                maxpos = i
            if minK <= nums[i] <= maxK:
                j = max(maxpos, minpos)
                if j <= lastout:
                    res += lastout - j
            else:
                lastout = i
        return res