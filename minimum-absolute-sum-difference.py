import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(nums1)
        order = sorted(nums1)
        res = float('inf')
        for i in range(n):
            j = bisect.bisect_left(order, nums2[i])
            for k in [j - 1, j, j + 1]:
                if 0 <= k < n:
                    res = min(res, abs(order[k] - nums2[i]) - abs(nums1[i] - nums2[i]))
        for i in range(n):
            res += abs(nums1[i] - nums2[i])
            res %= M
        return res