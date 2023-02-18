class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        if k == 0:
            if nums1 == nums2:
                return 0
            return -1
        pos = neg = 0
        for i in range(n):
            d = nums1[i] - nums2[i]
            if abs(d) % k != 0:
                return -1
            if d >= 0:
                pos += abs(d) // k
            else:
                neg += abs(d) // k
        if pos != neg:
            return -1
        return pos