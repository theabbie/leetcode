class Solution:
    def maxsum(self, nums1, nums2, i, n, mask):
        if i >= n:
            return 0
        key = (i, mask)
        if key in self.cache:
            return self.cache[key]
        res = float('inf')
        for j in range(n):
            if not mask & (1 << j):
                res = min(res, (nums1[i] ^ nums2[j]) + self.maxsum(nums1, nums2, i + 1, n, mask | (1 << j)))
        self.cache[key] = res
        return res
    
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        self.cache = {}
        return self.maxsum(nums1, nums2, 0, len(nums1), 0)