class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        m = len(nums1)
        n = len(nums2)
        for i in range(m):
            if n % 2 == 1:
                res ^= nums1[i]
        for j in range(n):
            if m % 2 == 1:
                res ^= nums2[j]
        return res