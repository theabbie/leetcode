from sortedcontainers import SortedList

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        bst = SortedList()
        res = 0
        p = 0
        for i in range(n + 1):
            res += bst.bisect_right(p - lower) - bst.bisect_left(p - upper)
            bst.add(p)
            p += nums[min(i, n - 1)]
        return res