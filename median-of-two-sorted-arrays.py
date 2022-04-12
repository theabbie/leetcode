class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = m + n
        total = sorted(nums1 + nums2)
        if k & 1:
            return total[(k - 1) // 2]
        else:
            return (total[(k - 1) // 2] + total[1 + (k - 1) // 2]) / 2