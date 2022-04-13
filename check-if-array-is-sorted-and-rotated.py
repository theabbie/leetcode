class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        pivot = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                pivot = i
                break
        for i in range(pivot, pivot + n - 1):
            if nums[(i + 1) % n] < nums[i % n]:
                return False
        return True