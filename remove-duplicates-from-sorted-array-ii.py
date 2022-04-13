class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                if ctr > 2:
                    nums[i] = None
                i += 1
            i += 1
        print(nums)
        i = 0
        while i < len(nums):
            if nums[i] == None:
                nums.pop(i)
            else:
                i += 1
        return len(nums)