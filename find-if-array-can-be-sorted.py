class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        ctr = lambda x: "{:0b}".format(x).count("1")
        for _ in range(n):
            for i in range(n - 1):
                if ctr(nums[i]) == ctr(nums[i + 1]) and nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums == sorted(nums)