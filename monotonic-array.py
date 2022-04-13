class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        grctr = 0
        lsctr = 0
        eqctr = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                grctr += 1
            elif nums[i] < nums[i - 1]:
                lsctr += 1
            else:
                eqctr += 1
        return grctr + eqctr == 0 or grctr + eqctr == n - 1 or lsctr + eqctr == 0 or lsctr + eqctr == n - 1