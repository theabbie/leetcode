class Solution:
    def minDel(self, nums, i = 0, switch = False, dels = 0):
        n = len(nums)
        if i >= n:
            if (n - dels) % 2 == 0:
                return 0
            return 1
        if switch:
            if i < n - 1 and i % 2 == 1 and nums[i] == nums[i + 1]:
                return 1 + self.minDel(nums, i = i + 1, switch = False, dels = dels + 1)
            return self.minDel(nums, i = i + 1, switch = True, dels = dels)
        else:
            if i < n - 1 and i % 2 == 0 and nums[i] == nums[i + 1]:
                return 1 + self.minDel(nums, i = i + 1, switch = True, dels = dels + 1)
            return self.minDel(nums, i = i + 1, switch = False, dels = dels)
    
    def minDeletion(self, nums: List[int]) -> int:
        return self.minDel(nums, i = 0, switch = False, dels = 0)