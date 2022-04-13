import bisect

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        op = []
        numset = set(nums)
        for num in numset:
            if bisect.bisect_right(nums, num) == bisect.bisect_left(nums, num) + 1:
                op.append(num)
        return op