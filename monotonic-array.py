class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        grctr = 0
        lsctr = 0
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                grctr += 1
            if nums[i] <= nums[i - 1]:
                lsctr += 1
        return grctr == 0 or grctr == n - 1 or lsctr == 0 or lsctr == n - 1