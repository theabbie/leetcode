import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        smallers = []
        for i in range(n - 1, -1, -1):
            currctr = bisect.bisect_left(smallers, nums[i])
            bisect.insort(smallers, nums[i])
            nums[i] = currctr
        return nums