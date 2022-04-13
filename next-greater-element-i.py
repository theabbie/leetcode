class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        greater = {}
        for i in range(n):
            for j in range(i + 1, n):
                if nums2[j] > nums2[i]:
                    greater[nums2[i]] = nums2[j]
                    break
        return [greater.get(num, -1) for num in nums1]