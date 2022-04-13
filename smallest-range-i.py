class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mn = float('inf')
        mx = float('-inf')
        for num in nums:
            mn = min(mn, num)
            mx = max(mx, num)
        return max(0, mx - mn - 2 * k)