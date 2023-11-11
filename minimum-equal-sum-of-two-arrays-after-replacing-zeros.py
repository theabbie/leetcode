class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = sum(nums1) + nums1.count(0)
        b = sum(nums2) + nums2.count(0)
        if a < b and nums1.count(0) == 0:
            return -1
        if b < a and nums2.count(0) == 0:
            return -1
        return max(a, b)