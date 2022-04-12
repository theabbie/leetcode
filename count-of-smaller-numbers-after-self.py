import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        smallers = []
        ctr = [0] * n
        for i in range(n - 1, -1, -1):
            currctr = bisect.bisect_left(smallers, nums[i])
            ctr[i] = currctr
            bisect.insort(smallers, nums[i])
        return ctr