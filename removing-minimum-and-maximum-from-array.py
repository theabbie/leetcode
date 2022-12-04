class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        a = min(nums)
        b = max(nums)
        i = nums.index(a)
        j = nums.index(b)
        i, j = min(i, j), max(i, j)
        return min(i + 1 + n - j, j + 1, n - i)