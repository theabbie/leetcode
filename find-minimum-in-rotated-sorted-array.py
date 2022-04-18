class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        beg = 0
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            if mid < n - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if beg >= end - 1:
                return nums[0]
            elif nums[mid] > nums[0]:
                beg = mid
            else:
                end = mid