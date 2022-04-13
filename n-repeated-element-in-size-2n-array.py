class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                i += 1
            i += 1
            if 2 * ctr == n:
                return nums[i - 1]