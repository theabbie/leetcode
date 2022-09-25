class Solution:
    def isCommon(self, X, Y, m, n, l):
        xset = set()
        for i in range(m - l + 1):
            xset.add(tuple(X[i:i+l]))
        for i in range(n - l + 1):
            if tuple(Y[i:i+l]) in xset:
                return True
        return False
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        beg = 0
        end = min(m, n)
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            if self.isCommon(nums1, nums2, m, n, mid):
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res