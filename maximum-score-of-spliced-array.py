class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        n1 = 0
        n2 = 0
        minyet = 0
        maxyet = 0
        maxdiff = 0
        mindiff = float('inf')
        for i in range(n):
            n1 += nums1[i]
            n2 += nums2[i]
            maxdiff = max(maxdiff, n1 - n2 - minyet)
            mindiff = min(mindiff, n1 - n2 - maxyet)
            if n1 - n2 < minyet:
                minyet = n1 - n2
            if n1 - n2 > maxyet:
                maxyet = n1 - n2
        return max(n1 - mindiff, n2 + maxdiff)