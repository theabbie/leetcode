class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        seq = sorted(range(n), key = lambda x: nums2[x])
        res = [-1] * n
        nums1.sort()
        i = 0
        unused = []
        for j in seq:
            while i < n and nums1[i] <= nums2[j]:
                unused.append(nums1[i])
                i += 1
            if i < n:
                res[j] = nums1[i]
                i += 1
            else:
                res[j] = unused.pop()
        return res