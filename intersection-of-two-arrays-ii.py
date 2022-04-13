class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        d2 = {}
        for num in nums1:
            d1[num] = d1.get(num, 0) + 1
        for num in nums2:
            d2[num] = d2.get(num, 0) + 1
        common = set.intersection(set(d1.keys()), set(d2.keys()))
        ans = []
        for c in common:
            ans += [c] * min(d1.get(c, 0), d2.get(c, 0))
        return ans