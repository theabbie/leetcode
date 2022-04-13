class Solution:
    def maxWig(self, nums, i, n, inc):
        if (i, inc) in self.cache:
            return self.cache[(i, inc)]
        maxSeq = 1
        for j in range(i + 1, n):
            if inc:
                if nums[j] > nums[i]:
                    maxSeq = max(maxSeq, 1 + self.maxWig(nums, j, n, False))
            else:
                if nums[j] < nums[i]:
                    maxSeq = max(maxSeq, 1 + self.maxWig(nums, j, n, True))
        self.cache[(i, inc)] = maxSeq
        return maxSeq
    
    def wiggleMaxLength(self, nums: List[int]) -> int:
        self.cache = {}
        n = len(nums)
        maxSeq = 1
        for i in range(n):
            maxSeq = max(maxSeq, self.maxWig(nums, i, n, True))
            maxSeq = max(maxSeq, self.maxWig(nums, i, n, False))
        return maxSeq