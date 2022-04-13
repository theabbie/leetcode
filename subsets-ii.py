class Solution:
    def gensets(self, nums, i, curr):
        if i == len(nums):
            self.subsets.add(tuple(curr))
            return
        self.gensets(nums, i + 1, curr)
        self.gensets(nums, i + 1, curr + [nums[i]])
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.subsets = set()
        self.gensets(nums, 0, [])
        return list(self.subsets)