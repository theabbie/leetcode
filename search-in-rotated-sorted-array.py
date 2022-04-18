class Solution:
    def getPivot(self, nums):
        n = len(nums)
        beg = 0
        end = n
        while beg <= end:
            mid = (beg + end) // 2
            if mid < n - 1 and nums[mid] > nums[mid + 1]:
                return mid + 1
            if beg >= end - 1:
                return 0
            elif nums[mid] > nums[0]:
                beg = mid
            else:
                end = mid
                
    def binarySearch(self, nums, beg, end, target):
        while beg <= end:
            mid = (beg + end) // 2
            if mid >= end:
                break
            elif nums[mid] == target:
                return mid
            elif beg == end:
                break
            elif nums[mid] > target:
                end = mid
            else:
                beg = mid + 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = self.getPivot(nums)
        left = self.binarySearch(nums, 0, k, target)
        if left != -1:
            return left
        right = self.binarySearch(nums, k, n, target)
        if right != -1:
            return right
        return -1