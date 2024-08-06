from collections import defaultdict

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        pos = defaultdict(list)
        for i in range(len(nums1)):
            pos[nums1[i]].append(i)
        res = 0
        prev = defaultdict(int)
        for j in range(len(nums2)):
            curr = defaultdict(int)
            for i in pos[nums2[j]]:
                curr[i] = 1 + prev[i - 1]
                res = max(res, curr[i])
            prev = curr
        return res