import bisect

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        numset = set(nums)
        for num in numset:
            if bisect.bisect_left(nums, num) + 1 == bisect.bisect_right(nums, num):
                return num