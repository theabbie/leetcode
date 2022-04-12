class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i == 0:
            nums.reverse()
            return
        mdiff = float('inf')
        closest = None
        for j in range(i, n):
            if nums[j] > nums[i - 1] and nums[j] - nums[i - 1] <= mdiff:
                mdiff = nums[j] - nums[i - 1]
                closest = j
        if closest:
            nums[i - 1], nums[closest] = nums[closest], nums[i - 1]
        for j in range(i, (i + n) // 2):
            nums[j], nums[n - j + i - 1] = nums[n - j + i - 1], nums[j]