class Solution:
    def maxp(self, a, b, i, j, empty, m, n):
        if i >= m or j >= n:
            if empty:
                return float('-inf')
            return 0
        key = (i, j, empty)
        if key in self.cache:
            return self.cache[key]
        x = self.maxp(a, b, i + 1, j, empty, m, n)
        y = self.maxp(a, b, i, j + 1, empty, m, n)
        z = a[i] * b[j] + self.maxp(a, b, i + 1, j + 1, False, m, n)
        res = max(x, y, z)
        self.cache[key] = res
        return res
    
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.cache = {}
        return self.maxp(nums1, nums2, 0, 0, True, len(nums1), len(nums2))