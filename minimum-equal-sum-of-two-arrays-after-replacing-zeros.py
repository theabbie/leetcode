class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        x = nums1.count(0)
        y = nums2.count(0)
        a = sum(nums1) + x
        b = sum(nums2) + y
        if (a > b and y == 0) or (b > a and x == 0):
            return -1
        return max(a, b)