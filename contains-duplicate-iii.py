from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        bst = SortedList()
        for i in range(n - 1):
            bst.add(nums[i])
            if i >= indexDiff:
                bst.remove(nums[i - indexDiff])
            if bst.bisect_right(nums[i + 1] + valueDiff) - bst.bisect_left(nums[i + 1] - valueDiff) > 0:
                return True
        return False