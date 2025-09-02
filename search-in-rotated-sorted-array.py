class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        beg = 0
        end = len(nums) - 1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] >= nums[0]:
                beg = mid + 1
            else:
                end = mid - 1
        end = beg + n - 1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid % n] <= target:
                beg = mid + 1
            else:
                end = mid - 1
        if nums[(beg - 1) % n] != target:
            return -1
        return (beg - 1) % n