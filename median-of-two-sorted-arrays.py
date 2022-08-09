class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        a = None
        b = None
        va = None
        vb = None
        if (m + n) & 1:
            a = b = (m + n - 1) // 2
        else:
            b = (m + n) // 2
            a = b - 1
        i = 0
        j = 0
        while va == None or vb == None:
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                if i + j == a:
                    va = nums1[i]
                if i + j == b:
                    vb = nums1[i]
                i += 1
            if j < n and (i >= m or nums2[j] < nums1[i]):
                if i + j == a:
                    va = nums2[j]
                if i + j == b:
                    vb = nums2[j]
                j += 1
        return (va + vb) / 2