import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        first = min(bisect.bisect_left(nums, target), len(nums) - 1)
        last = max(bisect.bisect_right(nums, target) - 1, 0)
        return [first if nums[first] == target else -1, last if nums[last] == target else -1]