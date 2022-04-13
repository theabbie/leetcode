class Solution:
    def reverse(self, nums, a, b):
        n = b - a
        for i in range(n // 2):
            nums[a + i], nums[a + n - i - 1] = nums[a + n - i - 1], nums[a + i]
        return nums
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = n - k % n
        self.reverse(nums, 0, k)
        self.reverse(nums, k, n)
        self.reverse(nums, 0, n)
        return nums