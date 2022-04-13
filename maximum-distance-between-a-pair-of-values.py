# class Solution:
#     def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
#         mdiff = 0
#         m = len(nums1)
#         n = len(nums2)
#         nums1min = [0] * m
#         nums2max = [0] * n
#         curr = 0
#         for i in range(m):
#             if nums1[i] < nums1[curr]:
#                 curr = i
#             nums1min[i] = curr
#         curr = n - 1
#         for i in range(n - 1, -1, -1):
#             if nums2[i] > nums2[curr]:
#                 curr = i
#             nums2max[i] = curr
#         print()
#         k = min(m, n)
#         for i in range(k):
#             mdiff = max(mdiff, nums2max[i] - nums1min[i])
#         return mdiff

import bisect

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        mdiff = 0
        m = len(nums1)
        n = len(nums2)
        nums2.reverse()
        for i in range(m):
            j = n - bisect.bisect_left(nums2, nums1[i]) - 1
            mdiff = max(mdiff, j - i)
        return mdiff