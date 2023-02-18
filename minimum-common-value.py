class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if len(common) == 0:
            return -1
        return min(common)