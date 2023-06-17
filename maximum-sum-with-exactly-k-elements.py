class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return k * m + k * (k - 1) // 2