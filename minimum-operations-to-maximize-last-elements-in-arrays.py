class Solution:
    def count(self, arr1, val1, arr2, val2):
        n = len(arr1)
        res = 0
        for i in range(n - 1):
            if arr1[i] > val1:
                if arr2[i] > val1:
                    res = float('inf')
                    break
                if arr1[i] > val2:
                    res = float('inf')
                    break
                res += 1
            elif arr2[i] > val2:
                if arr1[i] > val2:
                    res = float('inf')
                    break
                if arr2[i] > val1:
                    res = float('inf')
                    break
                res += 1
        return res
    
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        res = min(self.count(nums1, nums1[-1], nums2, nums2[-1]), 1 + self.count(nums1, nums2[-1], nums2, nums1[-1]))
        if res == float('inf'):
            return -1
        return res