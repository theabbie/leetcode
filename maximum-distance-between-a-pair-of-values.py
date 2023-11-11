class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        vals = []
        for i, el in enumerate(nums1):
            vals.append((el, i, 0))
        for i, el in enumerate(nums2):
            vals.append((el, i, 1))
        vals.sort()
        res = 0
        minfirst = float('inf')
        for val, pos, t in vals:
            if t == 1:
                res = max(res, pos - minfirst)
            else:
                minfirst = min(minfirst, pos)
        return res