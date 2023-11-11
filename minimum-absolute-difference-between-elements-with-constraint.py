from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        i = 0
        bst = SortedList()
        res = float('inf')
        for j in range(n):
            while j - i >= x:
                bst.add(nums[i])
                i += 1
            k = bst.bisect_left(nums[j])
            for l in [k - 1, k, k + 1]:
                if 0 <= l < len(bst):
                    res = min(res, abs(nums[j] - bst[l]))
        return res