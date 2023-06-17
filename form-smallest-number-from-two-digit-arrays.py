class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = min(nums1), min(nums2)
        common = set.intersection(set(nums1), set(nums2))
        if len(common) > 0:
            return min(common)
        a, b = min(a, b), max(a, b)
        return 10 * a + b