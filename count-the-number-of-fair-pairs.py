from sortedcontainers import SortedList

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        bst = SortedList()
        res = 0
        for i in range(n):
            res += bst.bisect_right(upper - nums[i]) - bst.bisect_left(lower - nums[i])
            bst.add(nums[i])
        return res