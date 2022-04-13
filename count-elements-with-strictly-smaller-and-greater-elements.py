class Solution:
    def countElements(self, nums: List[int]) -> int:
        sm = min(nums)
        mx = max(nums)
        return len([num for num in nums if num > sm and num < mx])