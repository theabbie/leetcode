from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        nums1ctr = Counter([el * el for el in nums1])
        nums2ctr = Counter([el * el for el in nums2])
        res = 0
        for i in range(m):
            for j in range(i + 1, m):
                res += nums2ctr[nums1[i] * nums1[j]]
        for i in range(n):
            for j in range(i + 1, n):
                res += nums1ctr[nums2[i] * nums2[j]]
        return res