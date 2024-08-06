class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums2.sort()
        n = len(nums1)
        res = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                curr = [nums1[k] for k in range(n) if k != i and k != j]
                curr.sort()
                valid = True
                for k in range(n - 2):
                    if curr[k] - nums2[k] != curr[0] - nums2[0]:
                        valid = False
                        break
                if valid:
                    res = min(res, nums2[0] - curr[0])
        return res