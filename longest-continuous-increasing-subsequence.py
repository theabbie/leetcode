class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        mlen = 1
        while j < n:
            if j < n - 1 and nums[j] < nums[j + 1]:
                j += 1
            else:
                i = j + 1
                j = j + 1
            mlen = max(mlen, j - i + 1)
        return mlen