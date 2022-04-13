class Solution:
    def numTuples(self, k, i, n):
        if (i, k) in self.cache:
            return self.cache[(i, k)]
        if i == n - 1:
            ctr = self.nums[i].count(k)
            self.cache[(i, k)] = ctr
            return ctr
        else:
            ctr = 0
            for num in self.nums[i]:
                ctr += self.numTuples(k - num, i + 1, n)
            self.cache[(i, k)] = ctr
            return ctr
    
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        self.cache = {}
        self.nums = [nums1, nums2, nums3, nums4]
        return self.numTuples(0, 0, len(self.nums))