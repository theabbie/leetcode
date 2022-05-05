class Solution:
    def search(self, nums, target, cmp, ncmp):
        beg = 0
        end = len(nums)
        while beg <= end:
            mid = (beg + end) // 2
            if mid >= len(nums):
                break
            curr = nums[mid]
            prev = nums[mid - 1] if mid > 0 else curr - 1
            forw = nums[mid + 1] if mid < len(nums) - 1 else curr + 1
            if curr == target and cmp(prev, forw):
                return mid
            elif beg == end:
                break
            elif ncmp(curr):
                beg = mid + 1
            else:
                end = mid
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.search(nums, target, lambda p, f: p < target, lambda c: c < target),
            self.search(nums, target, lambda p, f: f > target, lambda c: c <= target)
        ]