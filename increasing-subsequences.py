class Solution:
    def getSeq(self, nums, i, n):
        if i >= n:
            return [[]]
        op = []
        used = set()
        for j in range(i + 1, n):
            if nums[j] >= nums[i] and nums[j] not in used:
                val = self.getSeq(nums, j, n)
                op += [[nums[i], nums[j]]]
                op += [[nums[i]] + v for v in val]
                used.add(nums[j])
        return op
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        op = []
        used = set()
        for i in range(n):
            if nums[i] not in used:
                op += self.getSeq(nums, i, n)
                used.add(nums[i])
        return op