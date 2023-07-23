import numpy as np

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        d = []
        M = 0
        mx = 0
        for i in range(n):
            d.append(nums1[i] - nums2[i])
            M = min(M, nums1[i] - nums2[i] - diff, nums1[i] - nums2[i])
            mx = max(mx, nums1[i] - nums2[i])
        M *= -1
        res = 0
        order = np.array([0] * (mx + M + 1))
        for i in range(n - 1, -1, -1):
            res += np.sum(order[d[i] - diff + M : mx + M + 1])
            order[d[i] + M] += 1
        return res