class Solution:
    def lis(self, nums, i):
        if i == 0:
            return 1
        if self.cache[i] != -1:
            return self.cache[i]
        mlen = 1
        for j in range(i):
            if nums[j] < nums[i]:
                curr = 1 + self.lis(nums, j)
                mlen = max(mlen, curr)
        self.cache[i] = mlen
        return mlen
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = [-1] * n
        mlen = 1
        for i in range(n):
            curr = self.lis(nums, i)
            mlen = max(mlen, curr)
        return mlen