from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bst = SortedList()
        res = [0] * n
        for i in range(n - 1, -1, -1):
            res[i] = bst.bisect_left(nums[i])
            bst.add(nums[i])
        return res