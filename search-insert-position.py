class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        beg = 0
        end = n - 1
        res = n
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] >= target:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res