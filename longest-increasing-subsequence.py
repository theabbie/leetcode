# class Solution:
#     def lisRec(self, nums, i, n):
#         if i == n - 1:
#             return 1
#         maxSeq = 0
#         for j in range(i + 1, n):
#             if nums[j] > nums[i]:
#                 msxSeq = max(maxSeq, 1 + self.lisRec(nums, j, n))
#             else:
#                 msxSeq = max(maxSeq, self.lisRec(nums, j, n))
#         return maxSeq
            
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         return self.lisRec(nums, 0, len(nums))

class Solution:
    def lislen(self, nums, i, n):
        if i == n - 1:
            return 1
        if i in self.cache:
            return self.cache[i]
        mlen = 1
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                mlen = max(mlen, 1 + self.lislen(nums, j, n))
        self.cache[i] = mlen
        return mlen
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = {}
        maxSeq = 1
        for i in range(n):
            maxSeq = max(maxSeq, self.lislen(nums, i, n))
        return maxSeq