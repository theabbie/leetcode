class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        seen = False
        for i in range(n):
            if i < n - 1:
                if nums[i] != i + 1:
                    return False
            else:
                if nums[i] != n - 1:
                    return False
        return True