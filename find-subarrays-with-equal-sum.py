class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        exists = set()
        for i in range(n - 1):
            curr = nums[i] + nums[i + 1]
            if curr in exists:
                return True
            else:
                exists.add(curr)
        return False