class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort(reverse = True)
        s = sum(nums)
        curr = 0
        for i in range(n):
            curr += nums[i]
            s -= nums[i]
            if curr > s:
                return nums[:i + 1]