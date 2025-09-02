class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = Counter()
        for x, y in nums1 + nums2:
            res[x] += y
        return sorted(res.items())