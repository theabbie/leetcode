class Solution:
    def partition(self, nums, val):
        res = 0
        for el in nums:
            if el >= val:
                res += 1
        return res
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        beg = min(nums)
        end = max(nums)
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            ctr = self.partition(nums, mid)
            if ctr >= k:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res