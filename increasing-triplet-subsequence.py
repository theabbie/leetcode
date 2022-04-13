class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        minval, maxval = min(nums), max(nums)
        for i in range(1, n - 1):
            if nums[i] > minval and nums[i] < maxval:
                if min(nums[:i]) < nums[i] and nums[i] < max(nums[i+1:]):
                    return True
        return False